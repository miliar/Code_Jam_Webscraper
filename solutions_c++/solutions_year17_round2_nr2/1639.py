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

int N, T;
pair<int,int> san[99];
char harp[] = {'_','R','O','Y','G','B','V'};

int main(){
	//R => 1
	//O => 2
	//Y => 3
	//G => 4
	//B => 5
	//V => 6
	
	cin >> T;
	
	string ans, tmp;
	int _i;
	
	FOR(tst, 1, T){
		ans = "";
		
		cin >> N;
		
		FOR(i, 1, 6){
			cin >> san[i].ff;
			san[i].ss = i;
		}
		
		sort(san+1, san+1+6);
		reverse(san+1, san+1+6);
		
		//~ FOR(i, 1, 3){
			//~ cout << san[i] << "  ";
		//~ }
		//~ cout << "\n";
		
		if(san[1].ff > san[2].ff + san[3].ff  &&  N != 1)
			ans = "IMPOSSIBLE";
		else{
			FOR(i, 1, san[1].ff){
				ans += harp[san[1].ss];
				
				if(san[2].ff != 0)
					ans += harp[san[2].ss], san[2].ff--;
				else if(san[3].ff != 0)
					ans += harp[san[3].ss], san[3].ff--;
			}
			
			tmp = "";
			
			_i = ans.length();
			
			FOR(i, 0, _i-1){
				tmp += ans[i];
				if(san[3].ff != 0)
					tmp += harp[san[3].ss], san[3].ff--;
				//~ tmp += ans[i];
			}
			
			ans = tmp;
		}
		
		if(N > 1  &&  ans[0] == ans[N-1]){
			while(1){}
		}
		
		cout << "Case #" << tst << ": " << ans << "\n";
	}
}
