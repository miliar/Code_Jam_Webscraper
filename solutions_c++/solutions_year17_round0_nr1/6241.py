#include <bits/stdc++.h>
using namespace std;
char s[1005];
int sum[1005];

void cal(int Case) {

    int n, k, cur = 0, ans = 0;
    scanf("%s", s);
    scanf("%d", &k);
    n = strlen(s);
    memset(sum, 0, sizeof sum);
    //printf("len = %d\n",n);
    for (int i = 0; i < n-k+1; i++) {
        int a = (s[i] == '+' ? 0 : 1);
        if ((cur + a) % 2 != 0) {
            cur++;
            ans++;
            sum[i+k-1]--;
        }
        cur += sum[i];
    }

    for (int i = n-k+1; i < n; i++) {
        int a = (s[i] == '+' ? 0 : 1);
        if ((cur+a) % 2 != 0) {
            printf("Case #%d: IMPOSSIBLE\n",Case);
            return ;
        }
        cur += sum[i];
    }
    printf("Case #%d: %d\n", Case, ans);
}
int main(){
    int t;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int i=0; i < t; i++) {
        cal(i+1);
    }
}
