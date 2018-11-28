#include <bits/stdc++.h>
#define NINF INT_MIN 
#define INF INT_MAX
#define ull unsigned long long
#define ld long double
#define ll long long
#define MOD 1000000007
#define REM 4
#define N 1000005
#define pll pair<ll,ll>
#define pb(x) push_back(x)
#define mset(a) memset(a,0,sizeof(a))
#define sc(x)  scanf("%c",&x)
#define si(a)  scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define mll map<ll,ll>
#define iosbase  ios_base::sync_with_stdio(false)
#define dbg(x) cout<<#x<<"="<<x<<endl;
using namespace std;
int main()
{

	int t,i,l,flag,cnt,k,cs,j;
	string str;
	bool impossible;
	cin>>t;
	cs=1;
	char ch;
	int temp;
	int counter;
	while(t--)
	{
		cnt=0;
		impossible=false;

		cin>>str;
		cin>>k;
		l=str.length();
		for(i=0;i<l-k+1;i++)
		{
			if(str[i]=='-')
			{
				cnt++;
				for(j=i;j<k+i;j++)
				{
					if(str[j]=='-')str[j]='+';
					else str[j]='-';
				}
			}
		}
		// dbg(str);
		for(i=0;i<l;i++)if(str[i]=='-')impossible=true;
		
		if(!impossible)
			cout<<"Case #"<<cs<<": "<<cnt<<endl;
		else 
			cout<<"Case #"<<cs<<": "<<"IMPOSSIBLE"<<endl;
		cs++;
	}
	return 0;
}