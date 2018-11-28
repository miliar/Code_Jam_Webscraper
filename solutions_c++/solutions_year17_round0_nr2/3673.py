// Template by [thunder_blade]
// IIIT ALLAHABAD
// includes :)

#include<bits/stdc++.h>
using namespace std;
#define TEST  int test_case; cin>>test_case; while(test_case--)
#define all(v) (v).begin(),(v).end()
#define fi  first
#define se  second
#define pb push_back
#define mp make_pair
#define ll long long int
#define SPEED ios_base::sync_with_stdio(false);  cin.tie(0);  cout.tie(0);
#define pi(x) printf("%d\n",x)
#define pl(x) printf("%lld\n",x)
#define pf(x) printf("%f\n",x)
#define ps(x) printf("%s\n",x)
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define sf(x) scanf("%f",&x)
#define ss(x) scanf("%s",x)
#define pis(x) printf("%d ",x)
#define pls(x) printf("%lld ",x)
#define pfs(x) printf("%f ",x)
#define pss(x) printf("%s ",x)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define mod 1000000007

int main()
{
	int i,j,t,m;
	si(t);
	FOR(m,1,t+1){
		int f=0, g=0;
		string st, ans="";
		cin>>st;
		int l = st.length();
		if(l==1){
			cout<<"Case #"<<m<<": "<<st<<endl;
			continue;
		}
		int cnt=0;
		j=l;
		FOR(i,0,l-1)
		{
			if(st[i]<=st[i+1])
				continue;
			else{
				for(j=i;j>=0;j--)
					if(st[i]!=st[j]){
						j++;
						break;
					}
				break;
			}
		}
		if(j<0)
			j=0;
		i=0;
		FOR(i,0,j)
				ans += st[i];
		if(i<l)
			ans += ((st[i]-1)>'0'?st[i]-1:'9');
		if(st[i]-1=='0')
			i++;
		FOR(j,i+1,l)
			ans+='9';
		cout<<"Case #"<<m<<": "<<ans<<endl;

	}
	return 0;
}