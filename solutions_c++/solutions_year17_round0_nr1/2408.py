#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define endl "\n"
#define PI acos(-1)
typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> ii;
typedef complex<double> base;

int t, k;
string s;

void flip(int i){
	for(int j = i; j < i+k; j++){
		if(s[j] == '-') s[j] = '+';
		else s[j] = '-';
	}
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin >> t;

	for(int caso = 1; caso <= t; caso++){
		int res = 0, res1 = 0, res2 = 0;
		cin >> s >> k;
		string s2 = s;
		for(int i = 0; i <= s.size()-k; i++){
			if(s[i] == '-'){
				flip(i);
				res1++;
			}
		}

		for(int i = s.size()-k+1; i < s.size(); i++){
			if(s[i] == '-'){
				res1 = -1;
				break;
			}
		}

		s = s2;
		for(int i = s.size()-1; i >= k-1; i--){
			if(s[i] == '-'){
				flip(i-k+1);
				res2++;
			}
		}

		for(int i = k-2; i >= 0; i--){
			if(s[i] == '-'){
				res2 = -1;
				break;
			}
		}

		if(res1 != -1 and res2 != -1){
			res = min(res1, res2);
		}
		else if(res1 == -1 and res2 != -1){
			res = res2;
		}
		else if(res1 != -1 and res2 == -1 ){
			res = res1;
		}
		else{
			res = -1;
		}

		cout << "Case #" << caso << ": ";
		if(res != -1){
			cout << res << endl;
		}
		else{
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
