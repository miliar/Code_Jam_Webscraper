#include<bits/stdc++.h> 
using namespace std;
int T,k,n,i,ans;
char s[1010];
bitset<1010>a,b;
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%s",s);
		scanf("%d",&k);
		n=strlen(s);
		ans=0;
		a.reset();
		b.reset();
		for(i=0;i<n;i++)a[i]=(s[i]=='-');
		for(i=0;i<k;i++)b[i]=1;
		for(i=0;i<=n-k;i++)
			if(a[i])a^=b<<i,ans++;
		printf("Case #%d: ",_);
		if(a.count())puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
}
