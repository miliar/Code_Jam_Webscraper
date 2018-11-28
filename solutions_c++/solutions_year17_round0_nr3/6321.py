#include <iostream>
#include <queue>

int calculateLHS(int new_index, std::vector<int>& v) {
    if (new_index <= 0)
        return 0;
    int cnt = -1, i = new_index;
    while (v.at(i) != 1) {
        cnt++;
        i--;
    }

    return i;
}

int calculateRHS(int new_index, std::vector<int>& v) {
    if (new_index >= v.size() - 1)
        return 0;
    int cnt = -1, i = new_index;
    while (v.at(i) != 1) {
        cnt++;
        i++;
    }

    return i;
}

/*
struct PossibleNext {
    int max;
    int index;
    int lhs;
    int rhs;

    PossibleNext(int index, int max, int lhs, int rhs) {
        this->max = max;
        this->index = index;
        this->lhs = lhs;
        this->rhs = rhs;
    }

    // 1 0 0 0 0 0 0 1 size is 8, ends are 0 and 7
    // 1 0 0 1 0 0 0 1 added index 3, candidates are now 5 and 1 (lhs = 2, rhs = 3)
    // 1 0 0 1 0 1 0 1 added index 5, candidates are now 1, 4, 6 (lhs = 1, rhs = 1)
    // 1 1 0 1 0 1 0 1 added index 1, candidates are now 2, 4, 6 (lhs = 0, rhs = 1)

    void addChildren(std::priority_queue<PossibleNext>& heap, std::vector<int>& v) {
        // calculate sides
        // insert if valid
        int lower_bound = index - lhs;
        if (lhs != 0)
            lower_bound--;

        int left_candidate = (lower_bound + index) / 2;

        if (lower_bound > 0 && v.at(left_candidate) != 1) {\
            int lhs_temp = calculateLHS(left_candidate, v);
            int rhs_temp = calculateRHS(left_candidate, v);
            int max_temp = std::max(lhs_temp, rhs_temp);
            heap.push(PossibleNext(max_temp, left_candidate, lhs_temp, rhs_temp));
            v.at(left_candidate) = 1;
        }

        int upper_bound = index + rhs + 1;
        if (rhs != 0)
            upper_bound++;

        int right_candidate = (upper_bound + index) / 2;

        if (upper_bound < v.size() - 1 && v.at(right_candidate) != 1) {
            int lhs_temp = calculateLHS(right_candidate, v);
            int rhs_temp = calculateRHS(left_candidate, v);
            int max_temp = std::max(lhs_temp, rhs_temp);
            heap.push(PossibleNext(max_temp, right_candidate, lhs_temp, rhs_temp));
            v.at(right_candidate) = 1;
        }

        return;
    }

    bool operator>(const PossibleNext& rhs) {
        return max > rhs.max;
    }
};
*/
int main() {
    int tests;
    std::cin >> tests;

    int stallcnt, occupants;
    for (int i = 0; i < tests; i++) {
        std::cin >> stallcnt >> occupants;

        int leftVal, rightVal;
        if (stallcnt != occupants) {

            std::priority_queue<int> subarrays;
            subarrays.push(stallcnt);

            // 0 0 1 0 0 0 (2, 3)
            // 0 0 1 0 0 (2, 2)
            // 0 1 0 0 (1, 2)
            // 0 1 0 (1, 1)
            // 1 0 (0, 1)
            // 1 (0 , 0)
            while (occupants != 0) {
                int lhs, rhs;
                int current = subarrays.top();
                subarrays.pop();

                if (current % 2 == 1) { // odd
                    lhs = current / 2;
                    rhs = current / 2;
                } else {
                    lhs = current / 2 - 1;
                    rhs = current / 2;
                }

                occupants--;
                if (occupants == 0) {
                    leftVal = std::max(lhs, rhs);
                    rightVal = std::min(lhs, rhs);
                } else {
                    subarrays.push(lhs);
                    subarrays.push(rhs);
                }
            }
        } else {
            leftVal = 0;
            rightVal = 0;
        }

        std::cout << "Case #" << i + 1 << ": " << leftVal << " " << rightVal << std::endl;

        /*
        if (stallcnt != occupants) {
            std::vector<int> stalls(stallcnt + 2, 0);
            stalls.at(0) = 1;
            stalls.at(stalls.size() - 1) = 1;
            std::priority_queue<PossibleNext> queue;
            int midpt = stallcnt / 2;
            int lhs = calculateLHS(midpt, stalls);
            int rhs = calculateRHS(midpt, stalls);
            queue.push(PossibleNext(std::max(lhs, rhs), midpt, lhs, rhs));

            while(occupants != 0) {




                occupants--;
            }
        }
         */
    }

    return 0;
}