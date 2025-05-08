def count_words(content: str = None) -> int:
    if content is None or content == "":
        return 0
    return len(content.split())

def count_characters(content: str = None) -> dict[str, int]:
    if content is None or content == "":
        return {}
    
    output = {}
    for chr in content:
        lower_case = chr.lower()
        if lower_case not in output:
            output[lower_case] = 0
        output[lower_case] += 1
    return output

def sort_counts_on(dict) -> int:
    return dict["num"]

def generate_sorted_count(counts: dict[str, int] = None) -> list[dict]:
    output = []
    for key in counts:
        output.append({"char": key, "num": counts[key]})
    output.sort(reverse=True, key=sort_counts_on)
    return output