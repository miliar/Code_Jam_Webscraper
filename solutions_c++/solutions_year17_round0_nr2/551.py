#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long
ll N;

vector<int> nv;

std::string solve(int p, int v) {
    if (p == nv.size()) {
        return "";
    }
    if (nv[p] <= v) {
        return "bad";
    }

    auto a = solve(p + 1, nv[p] - 1);
    if (a != "bad") {
        return std::string("") + (char)('0' + nv[p]) + a;
    }

    if (nv[p] - 1 <= v) {
        return "bad";
    }

    std::string out;
    out += (char)('0' + nv[p] - 1);
    for (int i = p + 1; i < nv.size(); ++i) {
        out += '9';
    }
    return out;

}


int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        cin>>N;

        nv.clear();
        while (N) {
            nv.push_back(N % 10);
            N /= 10;
        }
        nv = std::vector<int>(nv.rbegin(), nv.rend());

        std::string ans = solve(0, -1);
        while (ans[0] == '0') {
            ans = ans.substr(1);
        }

        printf("Case #%d: %s\n", t, ans.c_str());
    }
}

