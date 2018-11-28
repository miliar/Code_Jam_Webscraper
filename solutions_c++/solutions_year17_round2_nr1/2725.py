#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
#define MOD 1e9 + 7
#define ull unsigned long long
#define iloop(a,b) for(ll i = a; i < b; ++i)
#define jloop(a,b) for(ll j = a; j < b; ++j)
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define p(a) cout << a << "\n";
void solve()
{
	int t;
	ll d,n,k,a,b;
	double max_val;
	scanf("%d",&t);
	for(int i = 1; i <= t; ++i)
	{
		printf("Case #%d",i);
		printf(": ");
		max_val = -1;
		scanf("%lld %lld",&d,&n);
		for(int j = 0; j < n; ++j)
		{
			scanf("%lld %lld",&a,&b);
			max_val = max(max_val,(double)(d-a)/(double)b);
		}
		printf("%0.9f\n", (double)d/(double)max_val);
	}
}
int main()
{
	bool testing = true;
	/*std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);*/
	if(testing)
	{
		freopen("A-large.in","rt",stdin);
		freopen("output.txt","wt",stdout);
		int start = clock();
		solve();
		int end = clock();
	//	cout << "time: " << (end - start)/(double)(CLOCKS_PER_SEC)*1000 << " milliseconds\n";
	}
	else
	{
		solve();
	}
}