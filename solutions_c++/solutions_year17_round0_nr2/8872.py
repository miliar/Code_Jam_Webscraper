#include <iostream>
#include <string>


std::string simplify(std::string s) {
    int from = 1;
    bool checked = false;
    for (int i = 0; i < (int)s.size() - 1; i++) {
        from = i + 1;
        if (s[i] > s[i + 1]) {
            s[i] = s[i] - 1;
            checked = true;
            break;
        }
    }

    if (checked) {
        for (int i = from; i < s.size(); i++) {
            s[i] = '9';
        }
    }

    while (s.size() > 1 && s.front() == '0') {
        s.erase(0, 1);
    }


    return s;
}


std::string getAns(std::string s) {
    std::string ans = simplify(s);

    while (ans != simplify(ans)) {
        ans = simplify(ans);
    }

    return ans;
}


int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        std::string s;
        std::cin >> s;
        std::cout << "Case #" << i + 1 << ": " << getAns(s) << std::endl;
    }

    return 0;
}
