#include <cstdio>
#include <cstdlib>
#include <windows.h>
#include <cstring>
#include <algorithm>
#include <iostream>
#define PI acos(-1.0)
#define EPS 1e-6

using namespace std;

int dcmp(double x) { return x < -EPS ? -x : x > EPS; }


int N, C, M;

int s[3][1005];
int cnt[3];


void solve() {
    int ans1, ans2;
    ans1 = ans2 = 0;
    cnt[1] = cnt[2] = 0;
    memset(s,0,sizeof(s));
    scanf("%d%d%d",&N,&C,&M);
    for (int i = 0; i < M; ++i) {
        int a, b;
        scanf("%d%d",&a,&b);
        ++s[b][a];
        ++cnt[b];
    }
    //printf("*%d %d\n%d %d\n",s[1][1],s[1][2],s[2][1],s[2][2]);
    ans1 = s[1][1] + s[2][1];
    int dif = max(cnt[1]-s[1][1]-s[2][1],cnt[2]-s[2][1]-s[1][1]);
    //printf("diff = %d\n",dif);
    ans1 = ans1 + max(0,dif);

    for (int i = 2;i <= N; ++i) {
        int need1 = s[1][i]-(cnt[2]-s[2][i]);
        int need2 = s[2][i]-(cnt[1]-s[1][i]);
        if (need1 > 0 && need2 > 0) {
            ans2 += min(need1,need2);
        }
    }

    printf("%d %d\n",ans1,ans2);
    //system("pause");
    //Sleep(1000);
}


int main() {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
