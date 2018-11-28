#include <iostream> 
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define For(i , a , b) for (int i = a , _b = b ; i <= _b ; ++i)
#define Ford(i , a  ,b) for (int i = a , _b = b : i >= _b ; --i)
#define Rep(i , n) for (int i = 0 , _n = n ; i < _n ; ++i)
#define sz(A) ((int)A.size())
#define LL(x) (x << 1)
#define RR(x) ((x << 1) | 1)

typedef pair<int , int> pt;

void ReadData() {

}

void fail(int test) {
	cout << "Case #" << test << ": IMPOSSIBLE\n";
}

int n, c[6];
vector<string> f[6];
string res[1000 + 123];

bool cmp(int i, int j) {
	return sz(f[i]) < sz(f[j]);
}

void Process(int test) {
	cin >> n >> c[0] >> c[3] >> c[1] >> c[4] >> c[2] >> c[5];

	if (n % 2 == 0) {
		if (c[0] == c[4] && c[0] + c[4] == n) {
			string t = "";
			Rep(i,n / 2) {
				t += 'R';
				t += 'G';
			}
			cout << "Case #" << test << ": " << t << endl;
			return;
		}
		if (c[1] == c[5] && c[1] + c[5] == n) {
			string t = "";
			Rep(i,n / 2) {
				t += 'Y';
				t += 'V';
			}
			cout << "Case #" << test << ": " << t << endl;
			return;
		}
		if (c[2] == c[3] && c[2] + c[3] == n) {
			string t = "";
			Rep(i,n / 2) {
				t += 'B';
				t += 'O';
			}
			cout << "Case #" << test << ": " << t << endl;
			return;
		}
	}
	string t;
	Rep(i,6) f[i].clear();
	if (c[4] && c[0] - 1 < c[4]) return fail(test);
	if (c[4]) {
		string t = "";
		t += 'R'; c[0]--; 
		For(j,1,c[4]) {
			t += 'G';
			t += 'R';
			--c[0];
		}
		f[0].push_back(t);
	}
	
	while (c[0]) {
		--c[0];
		f[0].push_back("R");
	}

	if (c[5] && c[1] - 1 < c[5]) return fail(test);
	if (c[5]) {
		string t = "";
		t += 'Y'; c[1]--; 
		For(j,1,c[5]) {
			t += 'V';
			t += 'Y';
			--c[1];
		}
		f[1].push_back(t);
	}

	while (c[1]) {
		--c[1];
		f[1].push_back("Y");
	}
	if (c[3] && c[2] - 1 < c[3]) return fail(test);

	if (c[3]) {
		t = "";
		t += 'B'; c[2]--; 
		For(j,1,c[3]) {
			t += 'O';
			t += 'B';
			--c[2];
		}
		f[2].push_back(t);
	}
	
	
	while (c[2]) {
		--c[2];
		f[2].push_back("B");
	}
	
	Rep(i,3) c[i] = sz(f[i]);
	n = c[0] + c[1] + c[2];
	Rep(i,3) if (c[i] > (n ) / 2) return fail(test);

	int id[3];
	Rep(i,3) id[i] = i;
	sort(id , id + 3, cmp);
	int j = 0;
	int z = n;

	while (z) {
		Rep(i,3) if (c[id[i]]) {
			int k = id[i];
			res[j] = f[k].back(); 
			f[k].pop_back();
			--c[k];
			--z;
			j += 2;
			if (j >= n) j = 1;
			break;
		}
	}

	cout << "Case #" << test << ": ";
	Rep(i,n) cout << res[i]; cout << endl;

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
//	freopen("input.inp" , "r" , stdin);
	//freopen("output.out" , "w" , stdout);
	int test; cin >> test;
	For(i,1,test) {
		ReadData();
		Process(i);
	}	

	return 0;

}			