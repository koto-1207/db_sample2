from db_config import Message


def find_message():

    if __name__ == "__main__":
        id = input("取得したい番号を記入ください: ")
        msg = Message.get_by_id(id)
        print(msg.id, msg.user, msg.content, msg.pub_date)


if __name__ == "__main__":
    find_message()
