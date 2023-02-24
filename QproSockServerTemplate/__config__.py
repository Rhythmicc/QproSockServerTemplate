import os
import json
from QuickProject import user_root, user_lang, QproDefaultConsole, QproInfoString, _ask

enable_config = True
config_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../QproSockServerTemplate_config.json")
)

questions = {
    "host": {
        "type": "input",
        "message": "Please enter the address to listen to"
        if user_lang != "zh"
        else "请输入监听地址",
        "default": "0.0.0.0",
    },
    "port": {
        "type": "input",
        "message": "Please enter the port to listen to"
        if user_lang != "zh"
        else "请输入监听端口",
        "default": "8000",
    },
    'thread': {
        'type': 'input',
        'message': 'Please enter the number of threads to use'
        if user_lang != 'zh'
        else '请输入使用的线程数',
        'default': '8',
    },
}


def init_config():
    with open(config_path, "w") as f:
        json.dump(
            {i: _ask(questions[i]) for i in questions}, f, indent=4, ensure_ascii=False
        )
    QproDefaultConsole.print(
        QproInfoString,
        f'Config file has been created at: "{config_path}"'
        if user_lang != "zh"
        else f'配置文件已创建于: "{config_path}"',
    )


class QproSockServerTemplateConfig:
    def __init__(self):
        if not os.path.exists(config_path):
            init_config()
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def select(self, key):
        if key not in self.config and key in questions:
            self.update(key, _ask(questions[key]))
        return self.config[key]

    def update(self, key, value):
        self.config[key] = value
        with open(config_path, "w") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
