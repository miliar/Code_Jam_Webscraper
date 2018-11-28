#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

//#include <unordered_map>
//#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef long long ll;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second
typedef complex<double> point;
#define X first
#define Y second
//#define X real()
//#define Y imag()

template<class T> ostream& operator << (ostream &o, const vector<T> &t){
	o << "[" << SZ(t);
	bool f = false;
	foreach(t,it)
		o << (f++ ? ", " : ": ") << (*it);
	return o << "]";
}

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p){
	return o << "(" << p.FR << ", " << p.SC << ")";
}


set <pll> S;

void my_add(pll p){
	set <pll>::iterator it = S.lower_bound(pll(p.FR,0));
	if(it == S.end() || (it->FR) != p.FR){
		S.insert(p);
		return;
	}
	p.SC += it->SC;
	S.erase(it);
	S.insert(p);
}

int main(){
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	FOR(x,1,T+1){
		LL n, k, y, z;
		cin >> n >> k;
		S.clear();
		S.insert(pll(n,1));
		while(k){
			pll b = *S.rbegin();
			S.erase(b);
			LL m = min(k,b.SC);
			k -= m;
			b.SC -= m;
			if(b.SC)
				my_add(b);
			my_add(pll(b.FR/2,m));
			y = b.FR/2;
			my_add(pll((b.FR-1)/2,m));
			z = (b.FR-1)/2;
		}

		cout << "Case #" << x << ": " << y << ' ' << z << endl;
	}
	
	return 0;
}
