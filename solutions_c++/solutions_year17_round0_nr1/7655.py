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
vector<int> vishwaprabhu, antaryami;
string s;
char vala[] = {'+', '-'};

char gotta(int a, int bit_Data) {
    int index_Wali_kudi = 0;
    if (s[a] == '-')  index_Wali_kudi = 1;
    int rem = bit_Data % 2;
    return vala[index_Wali_kudi ^ rem];
}

void solve() {
    antaryami = vector<int>(N, 0);
    int resu = 0;
    for (int i = 0; i <= n - k; i++) {
        if (gotta(i, antaryami[i]) == '+')  continue;
        resu++;
        for (int j = i; j - i < k; j++) antaryami[j]++;
    }
    bool found_hua_ki_nahi = true;
    for (int i = n - k + 1; i < n; i++) if (gotta(i, antaryami[i]) == '-'){
        found_hua_ki_nahi = false;
        break;
    }    
    resu = (found_hua_ki_nahi ? resu : N);
    vishwaprabhu.push_back(resu);
}

int main(){

    
    scanf("%d", &t);
    while (testnum <= t) {
        cin >> s >> k;
        n = s.length();
        vishwaprabhu.clear();
        solve();
        reverse(s.begin(), s.end());
        solve();
        int res = min(vishwaprabhu[0], vishwaprabhu[1]);
        if (res == N)
            cout << "Case #" << testnum << ": " << "IMPOSSIBLE\n";
        else    cout << "Case #" << testnum << ": " << res << "\n";
        
        testnum++;
    }

    return 0;
}