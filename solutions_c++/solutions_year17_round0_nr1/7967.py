#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define ALL(v)v.begin(),v.end()
#define PB(v)push_back(v)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//
string in;
int K;

char opp(char c){
	return c == '+' ? '-' : '+';
}

void flip(int i, int j){
	for(int k = i ; k <= j ; k++)in[k] = opp(in[k]);
}

bool done(){
	for(int i =  0 ; i < in.size() ; i++)if(in[i] != '+')return false;
	return true;
}

int solve(){
	int n = in.size();
	int cnt;
	cnt=0;
	for(int i = 0 ; i < n - K + 1; i++){
		if(in[i] == '-'){
			cnt++;
			flip(i, i + K - 1);
		}
	}

	for(int i = 0 ; i < n ; i++){
		if(in[i] == '-'){
			return -1;
		}
	}

	return cnt;
}

int main(){
	FASTER;

	int t;
	cin >> t;
	int Case = 1;
	while(t--){
		cin >> in >> K ;
		int x = solve();
		cout  << "Case #" << (Case++) << ": ";
		if( x != -1){
			cout << x;
		}else{
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}


	return 0;
}
