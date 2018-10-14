import sys

class Chest(dict):
    def __hash__(self):
        return id(self)

def solve(instream):
    num_keys, num_chests = [int(x) for x in instream.readline().split(" ")]
    available_keys = [int(x) for x in instream.readline().split(" ")]
    chests = []
    for i in range(num_chests):
        info = [int(x) for x in instream.readline().split(" ")]
        chests.append(Chest({
            "key_type": info[0],
            "contained_keys": info[2:],
            "opened": False,
            "future_chests_can_be_opened": set(),
        }))
        assert len(chests[i]["contained_keys"]) == info[1]

    assert len(chests) == num_chests

    for checking_chest in chests:
        for opening_chest in chests:
            if checking_chest["key_type"] in opening_chest["contained_keys"]:
                opening_chest["future_chests_can_be_opened"].add(checking_chest)

    def link_future_chests(chest):
        for future_chest in list(chest["future_chests_can_be_opened"]):
            for farther_future_chest in list(future_chest["future_chests_can_be_opened"]):
                if farther_future_chest in chest["future_chests_can_be_opened"]:
                    continue

                chest["future_chests_can_be_opened"].add(farther_future_chest)
                link_future_chests(farther_future_chest)
                chest["future_chests_can_be_opened"].update(
                    farther_future_chest["future_chests_can_be_opened"]
                )

    [link_future_chests(x) for x in chests]

    result = []

    def open_chest(i):
        nonlocal available_keys
        nonlocal opened_chest
        chest = chests[i]
        assert not chest["opened"]

        result.append(i)
        available_keys.remove(chest["key_type"])
        chest["opened"] = True
        available_keys += chest["contained_keys"]
        opened_chest = True

    while True:
        opened_chest = False
        for i in range(num_chests):
            cur_chest = chests[i]
            if cur_chest["opened"]:
                continue

            if cur_chest["key_type"] not in available_keys:
                continue

            if cur_chest["key_type"] in cur_chest["contained_keys"]:
                open_chest(i)
                break

            if available_keys.count(cur_chest["key_type"]) > 1:
                open_chest(i)
                break

            if not any([x for x in chests
                        if not x["opened"]
                        and x is not cur_chest
                        and x["key_type"] == cur_chest["key_type"]]):
                open_chest(i)
                break

            if any(cur_chest["key_type"] in x["contained_keys"]
                   for x in cur_chest["future_chests_can_be_opened"]):
                open_chest(i)
                break

            # Open the chest if we can get back the key later
            if any(not chest["opened"] and
                   chest["key_type"] != cur_chest["key_type"] and
                   chest["key_type"] in available_keys and
                   any(cur_chest["key_type"] in x["contained_keys"]
                       for x in chest["future_chests_can_be_opened"])
                   for chest in chests):
                open_chest(i)
                break

        if not opened_chest:
            return "IMPOSSIBLE"

        if all(chest["opened"] for chest in chests):
            assert len(result) == num_chests
            return " ".join(str(x + 1) for x in result)


def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()
