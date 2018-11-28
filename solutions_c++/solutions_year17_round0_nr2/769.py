#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
#define LL long long

char s[1005];
int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%s",s);
        int len = strlen(s);
        for (int i=len-2; i>=0; i--) {
            if (s[i]>s[i+1]) {
                s[i] = s[i]-1;
                for (int j=i+1; j<len; j++) s[j] = '9';
            }
        }
        LL ans;
        sscanf(s,"%lld",&ans);
        printf("Case #%d: %lld\n",t,ans);
    }
	return 0;
}
