from base64 import b64decode, b64encode


class B64:
    @staticmethod
    def encode(text: str, steps: int = 10) -> str:
        encoded = text

        for _ in range(steps):
            encoded = b64encode(encoded.encode("utf-8")).decode("utf-8")

        return encoded
    
    @staticmethod
    def decode(base64str: str, steps: int = 10) -> str:
        decoded = base64str

        for _ in range(steps):
            decoded = b64decode(decoded.encode("utf-8")).decode("utf-8")

        return decoded
    

__all__ = ["B64"]