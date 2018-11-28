#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
#define pb push_back
#define mp make_pair
#define inff 100000
#define ff first
#define ss second
#define sz(x) ((int) (x).size())
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define rep(i,N) for(int i = 0;i < N;i++)
#define frep(i,a,b) for(int i = a;i <= b;i++)
#define pii pair<int , int>
#define pll pair<ll , ll>
#define vii vector<int>
#define vpii vector< pii >
#define fill(A,v) memset(A,v,sizeof(A))
#define setbits(x) __builtin_popcountll(x)
#define print(A,j,k) for(int ii=j;ii<k;ii++)cout<<A[ii]<<" ";cout<<"\n"
#define all(x) (x).begin(), (x).end()
#define gcd __gcd
#define CASES int t;cin>>t;while(t--)
#define FILE freopen("inp.txt" , "r" , stdin);
#define ld long double

const int MOD = 1e9 + 7;
const int N = 2e6 + 5;
const int K = (1 << 17) + 10;
const ll INF = 2e18 + 500;
const int inf = 2e9 + 500;
const int SQRT = 500;
const int lgN = 20;

int A[N] , L[N] , R[N];

int main(int argc, char const *argv[])
{

	int tt;
	cin >> tt;
	for (int t = 1;t <= tt;t++) {
		cout << "Case #" << t << ": ";

		int n , k;
		cin >> n >> k;
		
		priority_queue<int> PQ;
		PQ.push(n);
		pii ans;
		while (k--) {
			int x = PQ.top();
			PQ.pop();
			assert(x > 0);
			if (x % 2 == 1) {
				ans = {(x - 1) / 2 , (x - 1) / 2};
			}
			else {
				ans = {(x / 2) - 1 , x / 2};
			}
			PQ.push(ans.ff);
			PQ.push(ans.ss);
		}
		cout << max(ans.ff , ans.ss) << ' ' << min(ans.ff , ans.ss) << endl;
	}

	return 0;
}