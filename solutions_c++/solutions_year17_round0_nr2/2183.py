#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

int len;
std::string s;
std::vector<int> ve;
std::vector<int> res;

bool dfs(int pos, int x)
{
    if (pos == len) {
        return true;
    }
    if (-1 == x) {
        res[pos] = 9;
        return dfs(pos+1, -1), true;
    }
    for (int i = ve[pos]; i >= x; --i) {
        bool r;
        res[pos] = i;
        if (i == ve[pos]) {
            r = dfs(pos+1, i);
        } else {
            r = dfs(pos+1, -1);
        }
        if (true == r) {
            return r;
        }
    }
    return false;
}

int main()
{
    int T_T, t_t;
    std::cin >> T_T;
    for (t_t = 1; t_t <= T_T; ++t_t) {
        std::cout << "Case #" << t_t << ": ";
        std::cin >> s;
        len = s.length();
        ve.clear();
        res.clear();
        res.resize(len);
        for (int i = 0; i < len; ++i) {
            ve.push_back(s[i] - '0');
        }
        dfs(0, 0);
        bool tag = false;
        for (int i = 0; i < len; ++i) {
            if (res[i] != 0) {
                std::cout << res[i];
                tag = true;
            } else if (true == tag) {
                std::cout << 0;
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
