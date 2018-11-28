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

int N, K;
int T;
string s;

int main(){
	cin >> T;
	
	int ans;
	FOR(i, 1, T){
		cin >> s >> K;
		
		N = s.length();
		
		ans = 0;
		
		FOR(j, 0, N - K)
			if(s[j] == '-'){
				ans++;
				
				FOR(k, j, j+K-1)
					s[k] = (s[k] == '-' ? '+' : '-');
			}
		
		FOR(j, N-K, N-1)
			if(s[j] == '-')
				ans = -1;
		
		if(ans == -1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE\n";
		else
			cout << "Case #" << i << ": " << ans << "\n";
	}
}
