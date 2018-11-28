#include<bits/stdc++.h>
#define maxn 500009
#define inf 1000000007
#define llinf 1000000000000000007
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define mid(a,b) (a+b)/2
#define endl "\n"
#define sz size()
#define MOD 1000000007
#define M 100000
#define pii pair<int,int>
#define all(x) x.begin(),x.end()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
using namespace std;
typedef long long ll;
//priority_queue < pii, vector< pii >, greater< pii > > Q;



int a[maxn], dp[maxn];

int main(){
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
	int T;
	cin>>T;
	for(int q=1; q<=T; q++){
		memset(a, 0, sizeof(a));
		memset(dp, 0, sizeof(dp));
		string s;
		int k, sum = 0, f1 = 0, f2 = 0, ans1 = 0, ans2 = 0, tot = inf;
		cin>>s>>k;
		for(int i=0; i<s.sz; i++)
			a[i] = (s[i] == '+');
		for(int i=0; i<s.sz; i++){
			dp[i]^=dp[i-1];
			a[i]^=dp[i];
			if(a[i] == 0 && i<s.sz-k+1){
				ans1++;
				dp[i+k]^=1;
				dp[i]^=1;
				a[i]^=1;
			}
		}
		for(int i=0; i<s.sz; i++)
			if(!a[i])
				f1 = 1;
		memset(a, 0, sizeof(a));
		memset(dp, 0, sizeof(dp));

		for(int i=0; i<s.sz; i++)
			a[i] = (s[i] == '+');
		for(int i=s.sz-1; i>=0; i--){
			dp[i]^=dp[i+1];
			a[i]^=dp[i];
			if(a[i] == 0 && i >= k-1){
				ans2++;
				if(i>=k)
					dp[i-k]^=1;
				dp[i]^=1;
				a[i]^=1;
			}
		}
		for(int i=0; i<s.sz; i++)
			if(!a[i])
				f2 = 1;
		if(!f1)
			tot = min(tot, ans1);
		if(!f2)
			tot = min(tot, ans2);
		cout<<"Case #"<<q<<": ";
		if(tot == inf)
			cout<<"IMPOSSIBLE"<<endl;			
		else
			cout<<tot<<endl;
	}
	


return 0;
}

