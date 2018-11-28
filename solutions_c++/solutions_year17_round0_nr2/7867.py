#include <iostream>
#include <string>
#include <cassert>

bool rec(
        const std::string &in,
        std::string &res,
        int pos,
        bool deduced,
        char last
        )
{
    const int l = res.length();
    if (pos == l) {
        return true;
    }
    char probe = deduced ? '9' : in[pos];
    if (probe < last) {
        return false;
    }
    res[pos] = probe;
    if (rec(in, res, pos+1, deduced, probe)) {
        return true;
    }
    while (--probe >= last) {
        res[pos] = probe;
        if (rec(in, res, pos+1, true, probe)) {
            return true;
        }
    }
    return false;
}

std::string solve(const std::string &in)
{
    std::string res = in;
    assert(rec(in, res, 0, false, '0'));
    return res;
}

int main()
{
    int T;
    std::cin >> T;
    for (int i = 1; i <= T; ++i) {
        std::string N;
        std::cin >> N;
        std::cout << "Case #" << i << ": ";
        const auto res = solve(N);
        if (res[0] == '0') {
            std::cout << &(res.c_str()[1]);
        } else {
            std::cout << res;
        }
        std::cout <<  '\n';
    }
    return 0;
}
