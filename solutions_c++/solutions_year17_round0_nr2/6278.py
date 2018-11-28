#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

long long ans=0, ten=1,n,m,a[30];
int i,j,k,DAT;
bool flag;

void dfs(int u, long long base, int MIN, long long pre)
{
	if (u>k) flag = true;
	for (int i=9;i>=MIN && !flag;i--)
	{
		if (pre+base*i>n) continue;
		a[u] = i;
		dfs(u+1, base/10, i, pre+i*base);
	}
}

int main() {
	cin>>DAT;
	for (int cas=1;cas<=DAT;cas++) {
		cin>>n;
		flag=false;
		m = n;
		k = 0;
		ans=0;
		ten=1;
		while (m>0) {
			m/=10;
			++k;
		}
		for (i=1;i<k;i++) ten*=10;
		memset(a,0,sizeof(a));
		dfs(1, ten, 0, 0);
		for (i=1;i<=k;i++)
		{
			ans+=a[i]*ten;
			ten/=10;
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}