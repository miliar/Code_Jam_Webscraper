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

constexpr int dx[4] = { 1, 0, -1, 0 };
constexpr int dy[4] = { 0, 1, 0, -1 };

#define SPRE(x) setprecision(x) // 精度を指定

void solve()
{
    int r,c;
    cin >> r >> c;
    vector<string> cake;
    vector<pair<int,int>> alpha;
    for(int i = 0; i < r;i++) {
        cake.push_back("");
        for(int j = 0; j < c; j++) {
            char t;
            cin >> t;
            cake[i] += t;
            if(t != '?')
                alpha.push_back({i,j});
        }
    }
    // for(int i = 0; i < cake.size(); i++) {
      //   for(int j = 0; j < cake[i].size(); j++) {
    for(auto A : alpha) {
        int i = A.first;
        int j = A.second;
        if(cake[i][j] != '?') {
            int p,q,d;
            p = j; q = j;
            p--; q++;
            // cerr << "IN " << i << ',' << j << ": p,q = " << p << ',' << q << '\n';
            while(p >= 0 && cake[i][p] == '?') cake[i][p--] = cake[i][j];
            while(q < cake[i].size() && cake[i][q] == '?') cake[i][q++] = cake[i][j];
            // cerr << "IN " << i << ',' << j << ": p,q = " << p << ',' << q << '\n';
            d = i + 1;
            while(d < cake.size()) {
                bool can = true;
                for(int l = p+1; l < q; l++)
                    if(cake[d][l] != '?') {
                         // cerr << d << ',' << l << "is not ?\n";
                        can = false;
                        break;
                    }
                if(!can)
                    break;
                for(int l = p+1; l < q; l++)
                    cake[d][l] = cake[i][j];
                d++;
            }
            d = i-1;
            while(d < cake.size()) {
                bool can = true;
                for(int l = p+1; l < q; l++)
                    if(cake[d][l] != '?') {
                         // cerr << d << ',' << l << "is not ?\n";
                        can = false;
                        break;
                    }
                if(!can)
                    break;
                for(int l = p+1; l < q; l++)
                    cake[d][l] = cake[i][j];
                d--;
            }
        }
    }
    cout << '\n';
    for(auto s : cake)
        cout << s << '\n';
}



int main()
{
	cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        std::cout << "Case #" << i + 1 << ":";
        solve();
    }
}

