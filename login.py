def login(username, password):
    if username == "admin" and password == "12345":
        return "Login successful"
    else:
        return "Invalid username or password"


print(login("admin", "12345"))