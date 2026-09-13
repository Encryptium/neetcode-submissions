class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty array"
        return "+-+".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "empty array":
            return []
        return s.split("+-+")