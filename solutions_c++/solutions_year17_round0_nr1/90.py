#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
#define mp make_pair    
const int MAXN = 1050;
int N, TC, K;
char s[MAXN];
bitset<MAXN> bs;
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%s%d",  s, &K);
        N = strlen(s);
        bs.reset();
        for (int i = 0; i < N; ++i) bs[i] = (s[i] == '+');
        int ans = 0;
        for (int i = 0; i <= N-K; ++i) {
            if (bs[i]) continue;
            ++ans;
            for (int j = i; j < i+K; ++j) 
                bs[j] = !bs[j];
        }
        bool pass = 1;
        for (int i = N-K; i < N && pass; ++i) {
            if (bs[i] == 0) pass = 0;
        }
        
        printf("Case #%d: ", Txn);
        if (pass) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
}