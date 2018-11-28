// Batman Is A Legend and Messi >>>>> CR7
	#include <bits/stdc++.h>

#define korn(i, n) for (long long int i = 0; i < (long long int)(n); i++)
#define kord(i, n) for ( long long int i = ( long long int)(n) - 1; i >= 0; i--)
#define korab(i, k, n) for (long long int i = ( long long int)(k); i < ( long long int)(n); i++)
#define korba(i, n, k) for ( long long int i = (long long int)(n) - 1; i >= ( long long int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<long long int> vi;
typedef pair<long long int,long long  int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-8;
const int INF = (int)1e9;
const int MAXN = 500500;

int T;
ll n, k;
pair<ll, ll> final;
map<ll, ll> ele;

int main() {

    cin >> T;
    korn(tt, T) {
        printf("Case #%d: ", tt + 1);
        
        cin >> n >> k;

		k--;
		ele.clear();
		ele[-n] = 1;
		final = {-1, -1};

		while (true) {
			pair<ll, ll> cur = *ele.begin();
			
			ll mat = -cur.X;
			ll cnt = cur.Y;

			ele.erase(cur.X);

			ll d1 = (mat - 1) / 2;
			ll d2 = mat / 2;
			
			k -= cnt;
			
			if (k < 0) {
				final = {d1, d2};
				break;
			}

			if (d1 > 0) {
				ele[-d1] += cnt;
			}
			if (d2 > 0) {
				ele[-d2] += cnt;
			}
		}		        

		assert(final.X != -1 && final.Y != -1);
		if (final.X < final.Y) {
			swap(final.X, final.Y);
		}

        cout << final.X << ' ' << final.Y << '\n';        
    }
    
    return 0;
}