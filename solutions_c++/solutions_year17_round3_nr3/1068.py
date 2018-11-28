/*input
4
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
2 1
0.0000
0.9000 0.8000
2 1
0.1000
0.4000 0.5000
*/
#include <bits/stdc++.h>
#define fastIo ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define fi first
#define se second
#define sz size
#define pb push_back
#define mp make_pair
using namespace std;

//#define LOCAL
#ifdef LOCAL
	#define DEBUG(x) do { cout << #x << ": " << x << '\n'; } while (0)
#else
	#define DEBUG(x) 
#endif

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;

const int dr[] = {1, 1, 0, -1, -1, -1, 0, 1};
const int dc[] = {0, 1, 1, 1, 0, -1, -1, -1};

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

double a[100005];

void solve(){
	int n, k;
	double u;
	cin >> n >> k >> u;

	for(int i = 0; i < n; i++){
		cin >> a[i];
	}
	sort(a, a + n);
	for(int i = 1 ; i < n ; i++){
    	double sum = (a[i] - a[i - 1]) * i ;
        if(sum <= u){
        	for(int j = 0; j < i; j++){
        		a[j] = a[i];
        	}
            u -= sum;
        }
        else{
        	for(int j = 0; j < i; j++){
        		a[j] += (u / (i * 1.0));
        	}
            u = 0.0;
            break;
        }
    }

    for(int i = 0; i < n; i++){
		a[i] += u / (n * 1.0);
    }

	double ans = 1.0;
	for(int i = 0; i < n; i++){
		ans *= a[i];
   	}

    cout << fixed << setprecision(12) << ans << '\n';
}

int main(){
	fastIo;
	
	freopen("C.in", "r", stdin);
	freopen("outC", "w", stdout);

	int t;
	cin >> t;

	for(int i = 0; i < t; i++){
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}