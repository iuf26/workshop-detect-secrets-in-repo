import json
from agent_framework import (
    handler, Executor, ChatAgent, WorkflowContext, 
)
from agent_framework.openai import OpenAIChatClient

from domain.models import (
    TextChunk, LineComment, 
    SecretsDetectorExecutorResponse, EmptySecretsDetectorExecutorResponseFactory, 
)
from domain.utils import chunk_consistency_helper

from domain.models import TextChunk

class SecretsDetectorExec(Executor):
    agent: ChatAgent
    agent_instruction = """
        <instruction role="system">
        You are a code-secrets detector. Given a text CHUNK (with "\n" newlines) and its original line interval [START, END], return only a JSON array of findings. Flag lines that contain likely secrets (API keys/tokens, private keys, passwords, connection strings with creds, service-account JSON fields, auth headers) or PII (names paired with email/phone/IDs). Be precise; if unsure, don't flag. Ignore obvious placeholders.
        </instruction>
        <schema>
        Output exactly:
        [
        { "line_number": <int original line>, "comment": "<types comma-separated>. Please remove." }
        ]
        Return [] if nothing is found. No extra text.
        </schema>
        <procedure>
        1) Split CHUNK by "\n".
        2) For each line i (1-based), assess for secrets/PII using field names and context (e.g., "api_key", "token", "password", "private_key", DSN with user:pass, "Authorization: Bearer ...", service-account fields like private_key_id/private_key).
        3) If flagged, compute original line_number = START + i - 1.
        4) Emit JSON as per <schema>, comments short, no code excerpts.
        </procedure>
        <example>
        INPUT:
        START=4, END=7
        CHUNK:
        print("ok")
        "private_key_id": "f4f3c2e1d0b9a8f7e6d5c4b3a2918171",
        print("done")

        OUTPUT:
        [
        { "line_number": 5, "comment": "Private key identifier. Please remove." }
        ]
        </example>
    """

    def __init__(self, chat_client: OpenAIChatClient,  my_shard: int, total_agents: int, id: str = "secrets detector"):
        #TODO: Here comes the code ;)
        return

    def create_prompt_from_chunk(self, chunk: TextChunk):
        prompt = f"""
            Please investigate and detect secrets existent in the chunk taken from the line intervals of the file {chunk.source_file}.
            INPUT
            START={chunk.line_span[0]}, END={chunk.line_span[1]}
            CHUNK:
            {chunk.text}
        """
        return prompt

    
    @handler
    async def run(self, chunk: TextChunk,ctx: WorkflowContext[SecretsDetectorExecutorResponse]) -> None:
        #TODO: Here comes the code ;)
        return