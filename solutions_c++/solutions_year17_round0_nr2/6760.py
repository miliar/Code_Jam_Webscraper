#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
vector<LL> Vec;

void dfs(LL val, int len) {
    if(len >= 19) return ;
    Vec.push_back(val);
    for(int i = val % 10; i < 10; i++) {
        dfs(val * 10 + i, len + 1);
    }
}

LL solve(LL num) {
    int id = lower_bound(Vec.begin(), Vec.end(), num) - Vec.begin();
    if(Vec[id] > num) return Vec[id - 1];
    return Vec[id];
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    Vec.clear();
    for(int i = 1; i <= 9; i++) dfs(i, 1);
    Vec.push_back(1111111111111111111LL);
    sort(Vec.begin(), Vec.end());
    //cout << Vec[Vec.size()-1] << endl;

    int T, cse = 1;
    scanf("%d", &T);
    while(T--) {
        LL num;
        scanf("%lld", &num);
        printf("Case #%d: %lld\n", cse++, solve(num));
    }
    return 0;
}
// 1000000000000000000
