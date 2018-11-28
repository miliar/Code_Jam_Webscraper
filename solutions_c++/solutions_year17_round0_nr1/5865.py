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

int solve()
{
    string st;
    int n;
    cin >> st >> n;
    int flip = 0;
    n--;
    for(int i = st.size() - 1; i >= n ; i--){
        if(st[i] == '-'){
            flip++;
            for(int j = 0; j <= n; j++)
                st[i-j] = st[i-j] == '+' ? '-' : '+';
        }
    }
    for (int i = 0; i < n; i++) {
        if(st[i] == '-')
            return -1;
    }
    return flip;
}


int main()
{
	cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        std::cout << "Case #" << i + 1 << ": ";
        int ans = solve();
        if(ans == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
}

