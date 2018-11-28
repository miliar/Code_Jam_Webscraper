#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define MAX 100000
#define pb push_back
#define mp make_pair
#define INF (1LL<<61)
#define MOD 1000000007
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
int main()
{
	Int T;
	cin>>T;
	for (Int k=1;k<=T;++k)
	{
		Int N,P,ans;
		cin>>N>>P;
		Int cnt[5]={0};
		for (Int i=0;i<N;++i)
		{
			Int G;
			cin>>G;
			cnt[G%P]++;
		}
		if (P==2)
		{
			if (cnt[1]==0)
				ans=cnt[0];
			else
				ans=cnt[0]+1+(cnt[1]-1)/2;
		}
		else if (P==3)
		{
			if (cnt[1]==0&&cnt[2]==0)
				ans=cnt[0];
			else if (cnt[1]==0)
				ans=cnt[0]+1+(cnt[2]-1)/3;
			else if (cnt[2]==0)
				ans=cnt[0]+1+(cnt[1]-1)/3;
			else if (cnt[1]<cnt[2])
				ans=cnt[0]+1+cnt[1]+(cnt[2]-cnt[1]-1)/3;
			else if (cnt[1]>cnt[2])
				ans=cnt[0]+1+cnt[2]+(cnt[1]-cnt[2]-1)/3;
			else
				ans=cnt[0]+cnt[1];
		}
		cout<<"Case #"<<k<<": "<<ans<<"\n";
	}
	return 0;
}