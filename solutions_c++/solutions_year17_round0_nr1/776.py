#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char s[1005];
int k;

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%s%d",s,&k);
        int len = strlen(s),ans = 0;
        for (int i=0; i<=len-k; i++) {
            if (s[i] == '-') {
                for (int j=0; j<k; j++)
                    if (s[i+j] == '-') s[i+j] = '+';
                    else s[i+j] = '-';
                ans++;
            }
        }
        int ok = 1;
        for (int i=0; i<len; i++)
            if (s[i] == '-') ok = 0;
        if (ok) {
            printf("Case #%d: %d\n",t,ans);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
    }
	return 0;
}
