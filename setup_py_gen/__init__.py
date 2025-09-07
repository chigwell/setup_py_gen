from llmatch_messages import llmatch
from langchain_llm7 import ChatLLM7
from langchain_core.language_models import BaseChatModel

from langchain_core.messages import SystemMessage, HumanMessage
from typing import Optional


def generate_setup_py_from_llm(
    llm: Optional[BaseChatModel],
    custom_text: str,
    package_name: str = None,
    author: Optional[str] = None,
    author_email: Optional[str] = None,
    repo_url: Optional[str] = None
) -> str:
    """
    Generate a plain setup.py script as a string using the provided ChatLLM7 instance.
    The function constructs a system message to instruct the model to output a valid
    setup.py file and provides the user's source code (custom_text) along with optional
    metadata (author, author_email, repo_url). It returns the generated setup.py code
    as a string. No file I/O or external network calls beyond the provided llm.
    """
    system = SystemMessage(content=(
        "You are a helpful assistant that outputs a valid Python setup.py script. "
        "Based on the provided source code and optional metadata, generate a single "
        "plain Python file named setup.py that is suitable for PyPI packaging. "
        "Return only the code, without explanations."
    ))
    metadata_parts = []
    if author:
        metadata_parts.append(f"Author: {author}")
    if package_name:
        metadata_parts.append(f"Package name: {package_name}")
    if author_email:
        metadata_parts.append(f"Author email: {author_email}")
    if repo_url:
        metadata_parts.append(f"Repo URL: {repo_url}")
    metadata_text = "\n".join(metadata_parts) if metadata_parts else "No metadata provided."

    human_content = (
        "Source/package description (custom_text):\n"
        f"{custom_text}\n\n"
        "Metadata:\n"
        f"{metadata_text}"
    )
    human = HumanMessage(content=human_content)

    response = llmatch(llm=llm, messages=[system, human], pattern=r"(?s)^(.*)$", verbose=True)

    if isinstance(response, dict) and response.get("success"):
        extracted = response.get("extracted_data") or []
        if extracted:
            return extracted[0]
        else:
            raise RuntimeError("LLM did not return setup.py code in extracted_data.")
    else:
        err = response.get("error_message") if isinstance(response, dict) else str(response)
        raise RuntimeError(f"LLM failed: {err}")
