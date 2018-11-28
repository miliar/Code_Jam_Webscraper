#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cctype>
#include <cassert>
#include <numeric>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>
#include <set>          
#include <map>
#include <unordered_set>
#include <cstdio>
#include <string>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>
#include <iomanip>

using namespace std;

const int N = 1e3 + 55;
int k, n, t, testnum = 1;
vector<int> ans, was;
string s;
char val[] = {'+', '-'};

char go(int a, int bit) {
    int index = 0;
    if (s[a] == '-')  index = 1;
    int rem = bit % 2;
    return val[index ^ rem];
}

void solve() {
    was = vector<int>(N, 0);
    int resu = 0;
    for (int i = 0; i <= n - k; i++) {
        if (go(i, was[i]) == '+')  continue;
        resu++;
        for (int j = i; j - i < k; j++) was[j]++;
    }
    bool found = true;
    for (int i = n - k + 1; i < n; i++) if (go(i, was[i]) == '-'){
        found = false;
        break;
    }    
    resu = (found ? resu : N);
    ans.push_back(resu);
}

int main(){
    
    scanf("%d", &t);
    while (testnum <= t) {
        cin >> s >> k;
        n = s.length();
        ans.clear();
        solve();
        reverse(s.begin(), s.end());
        solve();
        int res = min(ans[0], ans[1]);
        if (res == N)
            cout << "Case #" << testnum << ": " << "IMPOSSIBLE\n";
        else    cout << "Case #" << testnum << ": " << res << "\n";
        
        testnum++;
    }

    return 0;
}