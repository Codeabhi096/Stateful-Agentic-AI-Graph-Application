from configparser import ConfigParser


class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def _get_list(self, key):
        raw = self.config["DEFAULT"].get(key, "")
        return [item.strip() for item in raw.split(",") if item.strip()]

    def get_llm_options(self):
        return self._get_list("LLM_OPTIONS")

    def get_usecase_options(self):
        return self._get_list("USECASE_OPTIONS")

    def get_groq_model_options(self):
        return self._get_list("GROQ_MODEL_OPTIONS")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")