#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define ALL(v)v.begin(),v.end()
#define PB(v)push_back(v)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//
#define MAXN 2000
#define K first
#define S second

double T[MAXN];
vii H;

int main(){
	FASTER;
	int t;
	cin >> t;
	int D,N;
	int Case = 1;
	while(t--){

		cin >> D >> N;

		H.assign(N,ii());

		for (int i = 0; i < N; ++i) {
			cin >> H[i].K >> H[i].S;
		}

		sort(ALL(H));


		for(int i = N - 1; i >= 0 ; i--){

			double td = 1.0 * (D - H[i].K) / H[i].S;
			T[i] = td;

			for (int j = i+1; j < N; ++j) {

				if(H[i].S == H[j].S)continue;
				double tmp = 1.0 * (H[j].K - H[i].K) / (H[i].S - H[j].S);
				if(tmp < 1e-16)continue;

				// Does collide with Hj
				T[i] = max(T[i], T[j]);
			}

		}

		double ans = 0.0;
		double lo =0, hi = 1e17;

		for (int i = 0; i < 1000; ++i) {

			double mid = (lo + hi ) * 0.5;

			double tmp_t = D / mid;



			if(tmp_t >= T[0] - 1e-15 ){
				ans = mid;
				lo = mid;
			}else{
				hi = mid;
			}

		}

		cout << fixed << setprecision(10) << "Case #" << (Case++) << ": " << ans << endl;
	}

	return 0;
}
