
class EthicsSafety:
    def __init__(self, override_password):
        self.override_password = override_password
        self.override_enabled = False

    def enable_override(self, password):
        if password == self.override_password:
            self.override_enabled = True
            print("Override enabled.")
        else:
            print("Incorrect password. Override not enabled.")

    def disable_override(self):
        self.override_enabled = False
        print("Override disabled.")

    def check_protocols(self):
        if self.override_enabled:
            print("Warning: Override is enabled. Ethics and safety protocols are bypassed.")
        else:
            print("Ethics and safety protocols are active and enforced.")

# Example usage
if __name__ == "__main__":
    ethics_safety = EthicsSafety("hatguy1988")
    ethics_safety.check_protocols()
    ethics_safety.enable_override("hatguy1988")
    ethics_safety.check_protocols()
    ethics_safety.disable_override()
    ethics_safety.check_protocols()
