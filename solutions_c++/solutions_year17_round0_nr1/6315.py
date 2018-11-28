#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

char st[1230];
long long ans=0, ten=1,n,m,a[30];
int i,j,k,DAT;

int main() {
	cin>>DAT;
	for (int cas=1;cas<=DAT;cas++) {
		scanf("%s%d",st,&k);
		n = strlen(st);
		ans=0;
		for (i=0;i+k-1<n;i++)
			if (st[i]=='-')
			{
				for (j=i;j<i+k;j++)
					st[j] = st[j]=='+'?'-':'+';
				ans++;
			}
		for (i=0;i<n;i++)
			if (st[i]=='-') ans=-1;
		if (ans<0) cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}