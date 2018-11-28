#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#define N 1111
using namespace std;
int test,n,m,p[N],ans;
char str[N];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("q1.out","w",stdout);
	cin>>test;
	for (int tt=1;tt<=test;tt++)
	{
		printf("Case #%d: ",tt);
		ans=0;
		cin>>str>>m;
		n=strlen(str);
		for (int i=0;i<n;i++) if (str[i]=='-') p[i]=1;else p[i]=0;
		for (int i=0;i<=n-m;i++)
		if (p[i])
		{
			ans++;
			for (int j=i;j<i+m;j++)
			p[j]^=1;
		}
		for (int i=n-m+1;i<n;i++) if (p[i]) ans=0x3f3f3f3f;
		if (ans==0x3f3f3f3f) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
