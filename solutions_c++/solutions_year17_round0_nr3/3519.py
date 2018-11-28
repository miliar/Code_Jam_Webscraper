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
#include <bitset>

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
    int n, k;
    cin >> n >> k;
    int l = (int)pow(2,floor(log(k)/log(2))), sum = ((n - k) / l);
    if (sum % 2 == 0){
        cout << sum / 2 << " " << sum / 2 << endl;
    }
    else{
        cout << sum / 2 + 1 << " " << sum / 2 << endl;
    }
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
