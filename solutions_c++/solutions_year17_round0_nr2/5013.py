#include <iostream>
#include <unordered_set>
#include <string>
#include <cstddef>

std::string removeHeadingZeros(std::string& res) {
    std::size_t found = res.find_first_not_of('0'); 
    return res.substr(found); 
}

std::string helper(std::string n) {
    int l = n.size();
    std::string res;
    for (int i = 0; i < l - 1; i++) {
        if (n[i] <= n[i + 1]) {
            res.push_back(n[i]);
        } else {
            res.push_back(n[i] - 1);
            for (int j = i + 1; j < l; j++) {
                res.push_back('9');
            } 
            res = removeHeadingZeros(res);
            return res;
        }
    }

    res.push_back(n[l - 1]);
    res = removeHeadingZeros(res);
    return res;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; i++) {
        std::string n;
        std::cin >> n;
        std::string last = helper(n);
        std::string lastlast = helper(last); 
        while (last != lastlast) {
            //std::cout << last << ", " << lastlast << std::endl;
            last = lastlast;
            lastlast = helper(lastlast);
        }
        std::cout << "Case #" << i << ": " << last << std::endl;
    }
    return 0;
}

