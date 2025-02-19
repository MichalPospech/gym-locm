from gym_locm.engine.enums import ActionType


class Action:
    def __init__(self, action_type, origin=None, target=None, action_num=None):
        self.type = action_type
        self.origin = origin
        self.target = target
        self.number = action_num

    def __eq__(self, other):
        return (
            other is not None
            and self.type == other.type
            and self.origin == other.origin
            and self.target == other.target
        )

    def __repr__(self):
        if self.type == ActionType.PASS:
            return f"PASS {self.number}"
        elif self.type in (ActionType.PICK, ActionType.CHOOSE):
            return f"{self.type.name} {self.origin} {self.number}"
        else:
            return f"{self.type.name} {self.origin} {-1 if self.target is None else self.target} {self.number}"
