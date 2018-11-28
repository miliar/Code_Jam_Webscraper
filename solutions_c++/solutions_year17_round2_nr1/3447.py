#include <bits/stdc++.h>

using namespace std;

#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define ss(s)	scanf("%s",s)
#define ll long long
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
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vll;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vll>		vvl;

const ll mod = 2e18;
const int N = 3e5;

void solve(){

}

int main(int argc, char const *argv[])
{
	long long int T, count = 1, D, N, K[1001], S[1001], l, speed[1001];
	double sp, min = 0.0, rem;
	// For handling large inputs.
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cout <<setprecision(7) << fixed;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	// freopen("input.txt", "r", stdin);
	// freopen("output.txt", "r", stdout);
	cin >> T;
	while(T-- > 0) {
		cin >> D >> N;
		min = 0.0;
		sp = 0.0;
		for(long long int i = 0; i < N; i++){
			cin >> K[i] >> S[i];
			rem = D - K[i];
			sp = rem / S[i];
			if(sp > min)
				min = sp;
		}
		cout << "Case #" << count++ << ": ";
	    cout << D / min <<endl;	
	}
	return 0;
}