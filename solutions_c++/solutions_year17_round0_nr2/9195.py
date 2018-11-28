#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
using namespace std;
typedef long long LL;

void update(char *s,int i,int t){
    for(int j=i;j>=0;j--){
        s[j]='9';
    }
}

int main(int argc, char const *argv[])
{
	int T;
//	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("33","w",stdout);
	scanf("%d",&T);
	char s[20];
	for(int t=1;t<=T;t++){
		LL n;
		scanf("%lld",&n);
        memset(s,0,sizeof(s));
        LL m=n;
        int cnt=0;
        while(m){
            s[cnt++]=(m%10)+'0';
            m/=10;
        }
        int temp=s[0]-'0';
        for(int i=1;i<cnt;i++){
            if(s[i]>s[i-1]){
                s[i]--;
                update(s,i-1,s[i]-'0');
            }
        }
        LL ans=0;
        for(int i=cnt-1;i>=0;i--){
            ans=ans*10+(s[i]-'0');
        }
        printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}
