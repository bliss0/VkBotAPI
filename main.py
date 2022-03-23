import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard,VkKeyboardColor

session = vk_api.VkApi(token="a46498d3cb554e3d33d0bf78de9593142cd28dc4fe59e68ad0897cd129197ee454eb044161df03edc42a8")

def send_message(user_id, message,keyboard = None):
    post={
        "user_id":user_id,
        "message": message,
        "random_id": 0
    }
    if keyboard != None:
        post[keyboard]=keyboard.get_keyboard()
    else:
        post = post

    session.method("messages.send", post)



for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == "start":
            keyboard = VkKeyboard()
            keyboard.add_button("button", VkKeyboardColor.PRIMARY)

            send_message(user_id, "The first button", keyboard)
