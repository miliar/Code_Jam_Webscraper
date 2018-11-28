#include<bits/stdc++.h>
#define T() int t; cin>>t; while(t--)
#define f(i,start,lim) for(long long i=start;i<lim;i++)
#define ll long long
#define YES printf("YES\n")
#define NO printf("NO\n")
#define MOD 1000000007
#define MAX 9001
using namespace std;
int main()
{
	FILE *fin = freopen("a-small.in","r",stdin);
	assert(fin!=NULL);
	FILE *fout = freopen("a-output.out","w",stdout);
	int z=1;
	T()
	{
		double d,n;
		cin>>d>>n;
		double k[1000],s[1000],t ,tmax=0;
		f(i,0,n)
		{
			cin>>k[i]>>s[i];
			t = (d - k[i])/s[i];
			if(t  > tmax)
			tmax = t;
		}
		double res = d/tmax;
		cout<< "Case #"<<z<<": ";
		cout<<fixed<<setprecision(6)<<res<<endl;
		z++;
	}

}
