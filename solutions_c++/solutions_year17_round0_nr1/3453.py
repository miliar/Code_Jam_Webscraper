#include <iostream>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <vector>

#define ull unsigned long long
#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define iter iterator

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

const int inf = 1.01e9;
const double eps = 1e-9;

using namespace std;

void solve(){
    string s;
    int n;
    cin >> s >> n;
    int cnt = 0;
    for (int i = 0; i < s.length() - n + 1; ++i){
        if (s[i] == '-'){
            for (int j = i; j < i + n; ++j){
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
            ++cnt;
        }
    }
    for (int i = s.length() - n + 1; i < s.length(); ++i){
        if (s[i] == '-'){
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << cnt << endl;
}

int main(){
    //freopen("test.txt", "r", stdin);
    //freopen("ans.txt", "w", stdout);

    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i){
        cout << "Case #" << i << ": ";
        solve();
    }
}
