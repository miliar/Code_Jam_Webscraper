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
string s;
int k;

void ReadData() {
	cin >> s >> k;
}

void Process(int test) {
	int n = sz(s);
	s = ' ' + s;
	int res = 0;
	For(i,1,n - k + 1) {
		if (s[i] == '-') {
			For(j,i,i + k - 1) {
				if (s[j] == '-') s[j] = '+'; else s[j] = '-';
			}
			++res;
		}
	}
	For(i,1,n) if (s[i] == '-') {
		cout << "Case #" << test << ": " << "IMPOSSIBLE" << "\n";
		return;
	}
	cout << "Case #" << test << ": " << res << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	freopen("input.inp" , "r" , stdin);
	freopen("output.out" ,"w" , stdout);
	int test; cin >> test;
	For(i,1,test) {
		ReadData();
		Process(i);
	}

	return 0;

}			