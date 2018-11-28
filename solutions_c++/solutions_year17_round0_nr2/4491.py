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

bool isTidy(LL a){
	string s = to_string(a);
	return is_sorted(s.begin(), s.end());
}

LL solve(LL x){
	if(isTidy(x))
		return x;
	LL l = x, r = 0, p = 1;
	while(!isTidy(l)){
		r += 9*p;
		p *= 10;
		l = l/10;
	}
	LL ans = (l-1)*p+r;
	if (isTidy(ans))
		return ans;
	else
		return solve(ans);
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(test,1,T+1){
		LL x;
		cin >> x;
		cout << "Case #" << test << ": " << solve(x) << endl;
	}
	
	return 0;
}
