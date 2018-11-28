#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define sd(n) scanf("%lf",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define pb push_back
#define ll long long int
#define maxn 1005
#define sqrtn 317
#define maxm 51
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;
int arr1[3];
char arr[maxn];
std::vector<pii> v;

char col(int index)
{
	if(index==0)
	{
		return 'R';
	}
	if(index==1)
		return 'Y';
	return 'B';
}


int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		int n;
		si(n);
		int maxv=0;
		char c1,c2,c3;
		int co1,co2,co3;
		int num;
		v.clear();
		for(int i=0;i<3;i++)
		{

			si(arr1[i]);
			si(num);
			maxv=max(maxv,arr1[i]);
			v.pb(mp(arr1[i],i));
		}
		sort(v.begin(), v.end());
		co3=v[0].first;
		c3=col(v[0].second);

		co2=v[1].first;
		c2=col(v[1].second);

		co1=v[2].first;
		c1=col(v[2].second);

		if(maxv>n/2)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			int x=n-2*maxv;
			for(int i=0;i<3*x;i=i+3)
			{
				arr[i]=c1;
				arr[i+1]=c2;
				arr[i+2]=c3;
			}
			co3-=x;
			co2-=x;
			co1-=x;

			int flag=0;

			for(int i=3*x;i<n;i=i+2)
			{
				arr[i]=c1;
				if(co2!=0)
				{
					arr[i+1]=c2;
					co2--;
				}
				else
				{
					arr[i+1]=c3;
					co3--;
				}
			}
			for(int i=0;i<n;i++)
		{
			printf("%c",arr[i]);
		}
		ps("");
		}




	}
}