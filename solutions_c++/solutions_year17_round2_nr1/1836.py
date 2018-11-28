# include <bits/stdc++.h>

# define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
# define FORD(i, a, b) for(int i = (a); i >= (b); --i)
# define VAR(v, i) __typeof(i) v=(i)
# define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
# define ALL(x) (x).begin(), (x).end()
# define SZ(x) ((int)(x).size())
# define ff first
# define ss second
# define mp make_pair
# define pb push_back
# define next ____next
# define prev ____prev
# define left ____left
# define hash ____hash

using namespace std;

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<lld, lld> pll;

template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.first << ", " << pair.second << ")";}

// ---------------------------------------------------------------------------------------------------------------------------------- //

int N;
double pos;
double hiz;
double D;
double mx;

int T;

int main(){
	cin >> T;
	
	FOR(tst, 1, T){
		cin >> D >> N;
		
		mx = 0;
		
		FOR(i, 1, N){
			cin >> pos >> hiz;
			
			mx = max(mx, (D - pos) / hiz);
		}
		
		//~ cout << "Case #" << tst << ": " << D / mx;
		printf("Case #%d: %.7lf\n",tst, D/mx);
	}
}
