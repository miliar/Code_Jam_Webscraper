#include <iostream> 
#include <cstdio>
#include <iomanip>

using namespace std;

#define For(i , a , b) for (int i = a , _b = b ; i <= _b ; ++i)
#define Ford(i , a  ,b) for (int i = a , _b = b : i >= _b ; --i)
#define Rep(i , n) for (int i = 0 , _n = n ; i < _n ; ++i)
#define sz(A) ((int)A.size())
#define LL(x) (x << 1)
#define RR(x) ((x << 1) | 1)

typedef pair<int , int> pt;
const int maxn = 1000 + 123;
int d, n;
int k[maxn], s[maxn];
void ReadData() {
	cin >> d >> n;
	For(i,1,n) cin >> k[i] >> s[i];
}

const double INF = 1e9;
void Process(int test) {
	long double res = 0;
	For(i,1,n) {
		res = max(res, (long double)(d - k[i]) / s[i]);
	}

	long double v = d / res;
	cout << fixed << setprecision(6);

	cout << "Case #" << test << ": " << (double) v << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
		
	//freopen("input.inp" , "r" , stdin);
	//freopen("output.out" , "w" , stdout);
	int test; cin >> test;
	For(i,1,test) {
		ReadData();
		Process(i);
	}

	return 0;

}			