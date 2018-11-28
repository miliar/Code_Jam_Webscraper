#include <iostream> 
#include <cstdio>

using namespace std;

#define For(i , a , b) for (int i = a , _b = b ; i <= _b ; ++i)
#define Ford(i , a  ,b) for (int i = a , _b = b : i >= _b ; --i)
#define Rep(i , n) for (int i = 0 , _n = n ; i < _n ; ++i)
#define sz(A) ((int)A.size())
#define LL(x) (x << 1)
#define RR(x) ((x << 1) | 1)

typedef pair<int , int> pt;

long long n;
void ReadData() {
	cin >> n;
}

int nDigit(long long x) {
	int res = 0;
	while (x > 0) {
		res++; x /= 10;
	}
	return res;
}
long long pwr[20];

void Process(int test) {
	if (n <= 10) {
		cout << "Case #" << test << ": " << n << endl;
		return;
	}
	long long res = 0;
	int x = nDigit(n);
	For(i,1,x - 1) res = res * 10 + 9;
	pwr[0] = 1;
	For(i,1,18) pwr[i] = pwr[i - 1] * 10;
	long long cur = 0;
	int lastd = 0;
	for (int i = 18; i >= 1; i--) {
		int t = (n / pwr[i - 1]) % 10;
		int add = lastd;
		For(j,lastd,t) {
			bool ok = true;
			long long nex = cur;
			for (int k = i; k >= 1; k--) {
				nex = nex + pwr[k - 1] * j;
			}
			if (nex <= n) {
			 	ok = true;
			} else ok = false;
			if (ok) {
				add = j;
			}
		}
		cur = cur + pwr[i - 1] * add;
		lastd = add;
		
		if (add < t) {
			for (int k = i - 1; k >= 1; k--) {
				cur = cur + pwr[k - 1] * 9;
			}
			break;
		}
	}

	cout << "Case #" << test << ": " << max(res, cur) << endl;
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