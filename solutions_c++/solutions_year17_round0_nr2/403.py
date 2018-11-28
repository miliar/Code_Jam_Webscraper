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

char s[100];

int main() {
    //freopen("in","r",stdin);
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%s", s);
        int l = strlen(s);
        while(true)
        {
            bool flag = true;
            for(int i = 0; i < l - 1; i++)
            {
                if(s[i] > s[i + 1]) 
                {
                    s[i] = s[i] - 1;
                    for(int j = i + 1; j < l; j++) s[j] = '9';
                    flag = false;
                    break;
                }
            }
            if(flag) break;
        }
        printf("Case #%d: ", cas);
        ll res = 0;
        for(int i = 0; i < l; i++) res = res * 10 + s[i] - '0';
        printf("%lld\n", res);

    }
    return 0;
}
