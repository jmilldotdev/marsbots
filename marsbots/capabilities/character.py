from typing import Optional
from manifest import Manifest
from marsbots.util import generate_run_id


class CharacterCapability:
    def __init__(
        self,
        name: str,
        prompt: str,
        api_key: str,
        cache_connection: Optional[str] = None,
    ):
        self.name = name
        self.prompt = prompt
        self.llm = Manifest(
            client_name="openai",
            client_connection=api_key,
            cache_name="redis",
            cache_connection=cache_connection,
            max_tokens=100,
            temperature=1.0,
            stop_token="<",
        )

    def reply_to_message(self, message: str, sender_name: str):
        prompt = self.prompt
        prompt += "\n\n"
        prompt += f'<{sender_name}> "{message}"\n'
        prompt += f"<{self.name}>"
        completion = self.llm.run(prompt=prompt, run_id=generate_run_id())
        return completion
