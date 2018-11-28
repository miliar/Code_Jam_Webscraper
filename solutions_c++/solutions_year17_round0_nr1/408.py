#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;

char s[1005];
int k;

int main() {
    //freopen("in","r",stdin);
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%s%d", s, &k);
        int l = strlen(s);
        int ans = 0;
        for(int i = 0; i < l - k + 1; i++)
        {
            if(s[i] == '-') 
            {
                for(int j = i; j < i + k; j++)
                {
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+'; 
                }
                ans += 1;
            }
            else continue;
        }
        for(int i = 0; i < l; i++) if(s[i] == '-') ans = -1;
        printf("Case #%d: ", cas);
        if(ans != -1) printf("%d\n", ans);
        else puts("IMPOSSIBLE");

    }
    return 0;
}
