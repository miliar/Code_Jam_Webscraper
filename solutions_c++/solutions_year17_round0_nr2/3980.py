#include <bits/stdc++.h>
#define ll long long int
#define fio ios_base::sync_with_stdio(0);cin.tie(0)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
#define sc(t) scanf("%c",&t)
#define pb(x) push_back(x)
#define ii pair<int,int>
#define vi vector<int>
#define vvi vector<vi >
#define vii vector<ii >
#define vvii vector<vii >
#define clr(x) memset(x,0,sizeof(x))
#define rep(i,begin,end) for(__typeof(end) i=begin-(begin>end);i!=end-(begin>end);i+=1-2*(begin>end))
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define INF 101010101
#define MAX 100005
#define EPS 1e-12
using namespace std;

int main()
{
	int t; cin>>t;
	rep(z,1,t+1)
	{
		string s,ans;
		cin>>s;

		for(int i=0; i<s.length(); i++)
		{
			string temp = ans;
			while(temp.length() < s.length()) temp += s[i];
			if(stoll(temp) <= stoll(s)) ans += s[i];
			else
			{
				ans += (s[i]-1);
				while(ans.length() < s.length()) ans += '9';
				break;
			}
		}
		reverse(ans.begin(), ans.end());
		while(ans.back() == '0') ans.pop_back();
		reverse(ans.begin(), ans.end());

		cout<<"Case #"<<z<<": "<<ans<<"\n";
	}
	return 0;
}
