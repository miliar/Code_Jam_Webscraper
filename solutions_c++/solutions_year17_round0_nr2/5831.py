#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <iomanip>
#include <stack>
#include <fstream>
#include <cstdint>
#include <cmath>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

constexpr int INF       = 1000000000;/* 1e+9a */
constexpr int MODULO    = 1000000007;

typedef int64_t ll;

void solve()
{
    string s;
    cin >> s;
    for(int i = s.size() -1; i > 0; i--) {
        if(s[i] < s[i-1]) {
            int j = i;
            while(j < s.size())
                s[j++] = '9';

            j = i-1;
            while(j >= 0) {
                if(s[j] == '0') s[j--] = '9';
                else {
                    s[j]--;
                    break;
                }
            }
        }
    }
    if(s[0] == '0')
        cout << s.substr(1) << endl;
    else
        cout << s << endl;
}




int main()
{
	cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        std::cout << "Case #" << i + 1 << ": ";
        solve();
    }
}

