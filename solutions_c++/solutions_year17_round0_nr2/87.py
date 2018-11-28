#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
#define mp make_pair    
const int MAXN = 50;
int N, TC;
char s[MAXN], t[MAXN];
long long ans = 0;
bool r(int p, int x, bool same) {
    if (p == 0) {
        t[p] = x + '0';
        reverse(t, t+N);
        t[N] = 0;
        sscanf(t, "%lld", &ans);
        reverse(t, t+N);
        return 1;
    }
    t[p] = x + '0';
    for (int i = 9; i >= x; --i) {
        if (same && i > s[p-1] - '0') continue;
        if (r(p-1, i, same && i == (s[p-1] - '0'))) return 1;
    }
    return 0;
}
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        
        scanf("%s", s);
        N = strlen(s);
        reverse(s, s+N);
        ans = 0;
        r(N, 0, 1);
        
        //long long ans;
        //sscanf(s, "%lld", &ans);
        
        printf("Case #%d: ", Txn);    
        printf("%lld\n", ans);
    }
}