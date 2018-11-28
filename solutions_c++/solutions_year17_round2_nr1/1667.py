#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;


typedef long long ll;

typedef pair<int,int> pii;
typedef pair<ll, ll> pll;

const int maxn = 110;

int main(){
    // freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    int n;
    ll D, k, s;
    double ans;
    for (int i = 1; i <= t; i ++ ) {
        cin >> D >> n;
        cin >> k >> s;
        ans = D*s*1.0 / (D-k);
        for (int j = 2 ; j <= n; j ++ ){
            cin >> k >> s;
            ans = min(ans, D*s*1.0 / (D-k));
            }
        printf("Case #%d: %.6f\n", i, ans);
    }
    return 0;
}
