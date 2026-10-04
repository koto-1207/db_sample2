from db_config import Message


def display_all_message():
    message = Message.select()
    for msg in message:
        print(msg.id, msg.user, msg.content, msg.pub_date)


if __name__ == "__main__":
    display_all_message()
