#include <bits/stdc++.h>
#define PB push_back
#define FT first
#define SD second
#define MP make_pair
#define INF 0x3f3f3f3f
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int>  P;
const int N = 1e3 + 10,MOD = 7+1e9;
char s[N], k;
int main()
{
    freopen("E:\\ACM_code\\GCJ\\2017\\qua\\A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T, ca = 0;
    scanf("%d", &T);
    while(T --)
    {
        scanf("%s %d", s, &k);
        int ans = 0, len = strlen(s);
        bool flag = true;
        for(int i = 0;i < len;i ++)
        {
            if(s[i] == '+') continue;
            if(len - i < k) 
            {
                flag = false;
                break;
            }
            for(int j = 0;j < k;j ++)
                if(s[j + i] == '-') s[j + i] = '+';
                else s[j + i] = '-';
            ans ++;
        }
        if(!flag)
        {
            printf("Case #%d: IMPOSSIBLE\n", ++ ca);
        }
        else
        {
            printf("Case #%d: %d\n", ++ca, ans);
        }
    }
    return 0;
}