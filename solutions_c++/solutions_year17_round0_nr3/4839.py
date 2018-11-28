#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define ll long long
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define ss(s)	scanf("%s",s)
#define pi(x)	printf("%d\n",x)
#define pl(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, 0, sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pl;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pl>		vpl;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
int mpow(int base, int exp);
void ipgraph(int m);
void dfs(int u, int par);
const int mod = 1000000007;
const int N = 3e5, M = N;
//=======================

vi g[N];
int a[N];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int i,j,t,k,n;
	//freopen("in.txt", "r", stdin);	freopen("out.txt", "w", stdout);
	cin >> t;
	multiset<ll> my;
	ll hi, lo = 1, mid;
	fo(i, t){
		cin >> n >> k;
		my.clear();
		my.insert(n);
		if(k==n){
			cout << "Case #" << i+1 << ": 0 0"  << endl;
			continue;
		}
		k--;
		while(k--){
			hi = *my.rbegin();
			mid = (hi+1)/2;
			my.erase(my.find(hi));
			if(mid-1){
				my.insert(mid-1);
			}
			if(hi-mid){
				my.insert(hi-mid);
			}
		}
		hi = *my.rbegin();
		mid = (hi+1)/2;
		ll L = min(mid-1, hi-mid);
		ll R = max(mid-1, hi-mid);
		cout << "Case #" << i+1 << ": " << R << " " << L << endl;
	}

	return 0;
}
