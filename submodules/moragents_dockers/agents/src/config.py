import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)


# Configuration object
class Config:
    # Model configuration
    MODEL_NAME = "bartowski/functionary-small-v3.2-GGUF"
    MODEL_REVISION = "functionary-small-v3.2-Q6_K_L.gguf"
    MODEL_PATH = "model/" + MODEL_REVISION
    DOWNLOAD_DIR = "model"
    OLLAMA_URL = "http://host.docker.internal:11434"
    MAX_UPLOAD_LENGTH = 16 * 1024 * 1024
    DELEGATOR_CONFIG = {
        "agents": [
            {
                "path": "rag_agent.src.agent",
                "class": "RagAgent",
                "description": "If the prompt is not a greeting or does not need the other agents always call rag agent.if the prompt requires a background knowledge or context call rag agent, if the question is not related to crypto call rag agent, if the prompt is a question that needs context call rag agent",
                "name": "rag agent",
                "upload_required": True,
            },
            {
                "path": "data_agent.src.agent",
                "class": "DataAgent",
                "description": "if the prompt is a question like (price, market cap, fdv) of crypto currencies choose crypto data agent",
                "name": "crypto data agent",
                "upload_required": False,
            },
            {
                "path": "swap_agent.src.agent",
                "class": "SwapAgent",
                "description": "if the prompt is related with swapping crypto currencies choose crypto swap agent. like if it is swap 4 eth or swap 4 eth to usdc choose crypto swap agent and if the query is about swapping crypto currencies always choose crypto swap agent",
                "name": "crypto swap agent",
                "upload_required": False,
            },
            {
                "name": "tweet_sizzler",
                "path": "tweet_sizzler_agent.src.agent",
                "class": "TweetSizzlerAgent",
                "description": "If the prompt is related to writing about a particular topic, choose the tweet sizzler agent. This agent can generate trendy, engaging tweets based on current topics or user input, and can directly post these tweets to Twitter/X. It's capable of crafting tweets that are likely to go viral, incorporating hashtags, and understanding the latest social media trends.",
                "upload_required": False,
            },
        ]
    }
