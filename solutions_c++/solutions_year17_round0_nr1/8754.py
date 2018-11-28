#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define BUFF ios::sync_with_stdio(false);
#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl		//dbs(a _ b);
#define _ << ", " <<
#define endl '\n'
#define cl(x, v) memset((x), (v), sizeof(x))

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const double PI = acos(-1), EPS = 1e-9;
const long long LINF = 0x3f3f3f3f3f3f3f3fLL;
const int INF = 0x3f3f3f3f, MOD = 1e9+7, N = 1e5+5;

string s, temp;
int T, k, res;
char enter;

bool check(){
	for(int i=0; i<s.size(); i++)
		if(temp[i] == '-')
			return false;
	return true;
}

void flipping(int pos){
	for(int i=pos; i<pos+k; i++)
		if(temp[i] == '-')
			temp[i] = '+';
		else
			temp[i] = '-';
}

main(){
	BUFF;
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> s >> k;
		vi ord;
		for(int i=0; i<=s.size()-k; i++)
			ord.pb(i);
		res = INF;
		temp = s;
		if(check())
			res = 0;
		else{
			do{
				temp = s;
				for(int i=0; i<ord.size(); i++){
					flipping(ord[i]);
					if(check()){
						res = min(res, i+1);
						break;
					}
				}
	        	
	    	}while(next_permutation(ord.begin(), ord.end()));
		}

    	if(res == INF)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, res);

	}
}