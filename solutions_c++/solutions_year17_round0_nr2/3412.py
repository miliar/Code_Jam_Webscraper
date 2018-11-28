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

string best;

void rec(string s, int flag, int i){
    if (i == s.length()){
        best = s;
        return;
    }
    if (flag == 1){
        string s1 = s;
        s1[i] = '9';
        rec(s1, 1, i + 1);
    }
    else{
        if (s[i] == 0 || (i > 0 && s[i] < s[i - 1]))
            return;
        if (i == 0 || (i > 0 && s[i] > s[i - 1])){
            string s1 = s;
            s1[i] = s[i] - 1;
            rec(s1, 1, i + 1);
        }
        rec(s, 0, i + 1);
    }

}

void solve(){
    best = "";
    string s;
    cin >> s;
    rec(s, 0, 0);
    best = best.substr(best.find_first_not_of("0"));
    cout << best << endl;
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
