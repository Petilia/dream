import requests


def main():
    url = "http://0.0.0.0:8135/send"

    request_data = {
        "bot_utterances": [
            {
                "text": "Moving forward for 10 meters",
                "confidence": 1.0,
                "attributes": {"robot_command": "move_forward_10"},
            },
            {
                "text": "Moving backward for 10 meters",
                "confidence": 1.0,
                "attributes": {"robot_command": "move_backward_10"},
            }
        ],
        "dialog_ids": [
            "test_dialog_id",
            "test_dialog_id"
        ]
    }

    result = requests.post(url, json=request_data).json()
    print(result)
    gold_result = [{'human_attributes': {}}, {'human_attributes': {'performing_command': 'move_backward_10'}}]

    assert result == gold_result, f"Got\n{result}\n, but expected:\n{gold_result}"
    print("Success")


if __name__ == "__main__":
    main()
