#include <iostream>
#include <map>
#include <set>
#include <algorithm>

void process_one(std::map<long, std::set<long>> &stack, int cur, long *left, long *right) {
    if (stack.empty()) {
        // should not happen
        std::cerr << "error" << std::endl;
        return;
    }
    auto chose = --stack.end();
    auto pos = *(chose->second.begin());
    auto size = chose->first;
    chose->second.erase(chose->second.begin());
    if (chose->second.empty()) {
        stack.erase(chose);
    }
    auto chose_pos = pos + (size + 1) / 2 - 1;
    *left = chose_pos - pos;
    *right = size - *left - 1;
    if (left > 0) {
        auto left_it = stack.find(*left);
        if (left_it == stack.end()) {
            stack[*left] = {pos};
        } else {
            stack[*left].insert(pos);
        }
    }
    if (right > 0) {
        auto right_it = stack.find(*right);
        if (right_it == stack.end()) {
            stack[*right] = {chose_pos + 1};
        } else {
            stack[*right].insert(chose_pos + 1);
        }
    }
}


int main() {
    int loop;
    std::cin >> loop;
    //std::cout << loop << std::endl;
    for (int i = 0; i < loop; ++i) {
        long n, k;
        std::cin >> n >> k;
        std::map<long, std::set<long>> init_stack;
        std::set<long> init_set = {0};
        init_stack[n] = init_set;
        long left, right;
        for (int i = 0; i < k; ++i ) {
            process_one(init_stack, i, &left, &right);
        }
        std::cout << "Case #" << i + 1 << ": " << std::max(left, right) << " " << std::min(left, right) << std::endl;
        //std::cout << n << ", " << k << std::endl;
    }

    return 0;
}
