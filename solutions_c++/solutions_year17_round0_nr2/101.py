#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define LL long long
using namespace std;
int T_T;
char str[100];
int main(void)
{
//    freopen("B-large.in","r",stdin);
//    freopen("out-large.txt","w",stdout);
    scanf("%d",&T_T);
    for (int cas=1;cas<=T_T;cas++)
    {
        scanf("%s",str);
        int len = strlen(str), i;
        for (i=0;i<len-1;i++) if (str[i] > str[i+1]) break;
        if (i < len-1) {
            for (;i>0;i--) if (str[i] != str[i-1]) break;
            str[i]--;
            for (int j=i+1;j<len;j++) str[j] = '9';
        }
        char * ans;
        if (str[0] == '0') ans = str+1;
        else ans = str;
        printf("Case #%d: %s\n",cas,ans);
    }
    return 0;
}
