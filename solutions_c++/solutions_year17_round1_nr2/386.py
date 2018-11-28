#include <bits/stdc++.h>
#define N 64
#define NMAX 1000100

using namespace std;
typedef long long ll;
int t;
int n,m;
ll tab[N][N];
ll r[N];
ll s[N];
ll e[N];
ll laste[N];
ll lasts[N];
ll pointers[N];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>t;
	for(int c=1;c<=t;++c) {
		cin>>n>>m;
		for(int i=0;i<n;++i)
			cin>>r[i];
		for(int i=0;i<n;++i) {
			for(int j=1;j<=m;++j) {
				cin>>tab[i][j];
			}
			tab[i][0]=0;
		}
		m++;
		for(int i=0;i<n;++i)
		{
			sort(tab[i],tab[i]+m);
			lasts[i]=0;
			laste[i]=0;
		}
		for(int i=0;i<n;++i)
			pointers[i] = 0;
		ll sum = 0;
		bool check = true;
		for(ll p=1;p<=NMAX && check;++p) {
			for(int i=0;i<n;++i) {
				double si = 0.90*p*r[i];
				double ei = 1.10*p*r[i];
				lasts[i]=s[i];
				laste[i]=e[i];
				ll ii = si;
				if((double)ii==si)
					s[i] = ii;
				else s[i]=ii+1;
				ii=ei;
				e[i] = ii;
			}
			int minimum = 0x3f3f3f3f;
			for(int i=0;i<n;++i) {
				int cnt = 0;
				for(int j=pointers[i]+1;j<m;++j) {
					if(tab[i][j]>= s[i] && tab[i][j]<=e[i])
						cnt++;
				}
				minimum = min(minimum,cnt);
				if(s[i]>tab[i][m-1]) {
					check = false;
				}
			}

			if(minimum ==0 )continue;

			for(int i=0;i<n;++i) {
				int cnt = 0;
				for(int j=pointers[i]+1;j<m;++j) {
					if(tab[i][j]>= s[i] && tab[i][j]<=e[i])
					{
						cnt++;
						if(cnt==minimum) {
							pointers[i]=j;
							break;
						}
					}

				}
			}
			sum+=minimum;
		}
		cout<<"Case #"<<c<<": "<<sum<<endl;
	}
	return 0;
}