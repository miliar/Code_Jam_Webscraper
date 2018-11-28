#include <bits/stdc++.h>
using namespace std;

const int N=1005;
char s[N];
int f[N];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T,n,k;
    int ca=1;

    scanf("%d",&T);
    while (T--){
 
    memset(f,0,sizeof(f));

    scanf("%s%d",s,&k);

    int n=strlen(s);

    for (int i = 0; i < n; i ++) {
        if (s[i] == '+')
            f[i] = 1;
    }

    int ans=0;

    for (int i=0;i<n;i++){
    	if (f[i]%2==0){
    		if (i>n-k) {ans=n+1;break;}
    		for (int j=i;j<i+k;j++) f[j]++;
    		ans++;
    	}
    }

    printf("Case #%d: ",ca++);
    if (ans == n+1) puts("IMPOSSIBLE");
    else printf("%d\n",ans);
	}
    return 0;
}
