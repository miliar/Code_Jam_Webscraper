/**********************************************
            Author : smiley007  
***********************************************/

//Data Structure Includes
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>
#include <set>          
#include <map>
#include <unordered_set>

//Other Includes
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cctype>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>
#include <iomanip>

using namespace std ;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vvll> vvvll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<vpii> vvpii;
typedef vector<pll> vpll;
typedef vector<vpll> vvpll;
typedef vector<vvpll> vvvpll;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#ifdef LocalHost
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#endif

//Code Begins Here ------ >>>
const int N = 1e3 + 55;
string s;
int k, n;
int t, tt = 1;
vi ans;
char c[] = {'+', '-'};

char get(int idx, int tog) {
    int c_idx = 0;
    if (s[idx] == '-')  c_idx = 1;
    int rem = tog % 2;
    return c[c_idx ^ rem];
}

void solve() {
    int tog[N] = {0};
    int res = 0;
    for (int i = 0; i <= n - k; i++) {
        if (get(i, tog[i]) == '+')  continue;
        res++;
        for (int j = i; j - i < k; j++) tog[j]++;
    }
    bool ok = true;
    for (int i = n - k + 1; i < n; i++) if (get(i, tog[i]) == '-'){
        ok = false;
        break;
    }    
    res = (ok ? res : N);
    ans.push_back(res);
}

int main(){
    #ifdef LocalHost
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    
    scanf("%d", &t);
    while (tt <= t) {
        cin >> s >> k;
        n = s.length();
        ans.clear();
        solve();
        reverse(s.begin(), s.end());
        solve();
        int mn = min(ans[0], ans[1]);
        cout << "Case #" << tt << ": ";
        if (mn == N)    cout << "IMPOSSIBLE\n";
        else    cout << mn << "\n";
        tt++;
    }





    

    return 0;
}