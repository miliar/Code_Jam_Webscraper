#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

vi v;
int T;

int f(int u) {
	int j = u-1;
	while (v[j] == 0) j--;
	int x = j;
	j--;
	while (j >= 0 && v[j] == v[x]) {
		v[j]--;
		--j;
		--u;
	}
	v[x]--;

	for (int i = u; i<v.size(); i++)
		v[i] = 9;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin >> T;
	For(tt,1,T+1) {
		cout<< "Case #" << tt <<": ";
		string tmp; cin >> tmp;
		v.clear();
		For(i,0,tmp.size())
			v.pb(tmp[i]-'0');

		bool ok = false;
		for (int i = 1; i<v.size(); i++) {
			if (v[i] < v[i-1]) {
				f(i);
				break;
			}
		}
		for (int i = 0; i<v.size(); i++) {
			if (v[i] == 0 && !ok) continue;
			if (v[i] != 0) ok = true;
			cout << v[i];
		}
		cout << endl;
	}
	
	
	return 0;
}
