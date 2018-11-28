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

lld tap(lld x){
	vector<int> A;
	
	while(x){
		A.pb(x % 10);
		x /= 10;
	}
	
	reverse( ALL(A) );
	
	FORD(i, SZ(A)-2, 0)
		if(A[i] > A[i+1]){
			FOR(j, i+1, SZ(A)-1)
				A[j] = 9;
			
			A[i]--;
		}
	
	lld ret = 0;
	
	FOR(i, 0, SZ(A)-1){
		ret *= 10;
		ret += A[i];
	}
	
	return ret;
}

int main(){
	int T;
	lld x;
	
	cin >> T;
	
	FOR(i, 1, T){
		cin >> x;
		
		cout << "Case #" << i << ": " << tap(x) << "\n";
	}
}
