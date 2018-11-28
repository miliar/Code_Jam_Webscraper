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
const int N = 1010;

int n, m, c;

ii t[N];
int gc[N];
int cr[N], yG;

bool chk(int a) {
	
	vi cnt(n+1,0);
	int y = 0, av = 0;

	for (int i = 1; i<=n ;i++)
		av += max(0, a-cr[i]);

	yG = 0;
	//cout << a << "!!\n";
	for(int i = n ;i>0; i--) {

		int ym = min (y, max(0,a-cr[i]));
		yG += ym;
		y -= ym;

		av -= max(0, a-cr[i] - ym);

		if (cr[i] > a) { y += cr[i] - a;}


		//cout << y << " " << av << "!!!\n";
		if (y > av) return false;
		//av -= y;
	}
	yG += y;
	return true;
}

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;

	For(tt, 1, 1+T) {
		memset(gc, 0, sizeof gc);
		memset(cr, 0, sizeof cr);
		cin >> n >> c >> m;
		For(i,0,m){
			cin >> t[i].fi >> t[i].se;
			cr[t[i].fi]++;
			gc[t[i].se]++;
		}

		int lo = 0;
		for (int i = 1 ;i<=c ;i++)
			lo = max(gc[i], lo);

		//cout << "@@@" << lo << endl;
		int hi = m;

		while (lo != hi) {
			int mi = (lo+hi)/2;
			if (chk(mi))
				hi = mi;
			else lo = mi+1;
			//cout << mi << endl;
		}
		chk(lo);
		cout << "Case #" << tt <<": ";
		cout << lo << " " << yG << endl;
	}
	
	
	return 0;
}
