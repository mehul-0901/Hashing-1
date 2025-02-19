class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = defaultdict(list)
        for s in strs:
            count = [0]*26
            for st in s:
                count[ord(st)-ord("a")] += 1
            hash1[tuple(count)].append(s)
                
                
        return hash1.values()