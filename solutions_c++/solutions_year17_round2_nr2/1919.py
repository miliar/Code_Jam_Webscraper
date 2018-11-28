#include<bits/stdc++.h>
#define __SUBMIT__ ios_base::sync_with_stdio(0); \
                   cin.tie(0);
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int MOD = 1e9 + 7;
const int NMAX = 1e9;

char last(string s) {
	return s[s.size()-1];
}

int main()
{
    __SUBMIT__
    int TC; cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
    	int N, R, O, Y, G, B, V;
    	bool cont = true;
    	cin >> N >> R >> O >> Y >> G >> B >> V;
    	cout << "Case #" << tc << ": ";
    	string ans;

    	while (cont && O > 0) {
    		if (O == 1 && B >= 2) {
				ans += "BOB";
    			B -= 2;
    			O--;
    			N -= 3;
    		}

    		else if ((O == 1 && B == 1 && N == 2) || (O > 1 && B >= 1) ) {
    			ans += "BO";
    			B--;
    			O--;
    			N -= 2;
    		}
    		else {
    			cont = false;
    		}
    	}

    	while (cont && G > 0) {
    		if (G == 1 && R >= 2) {
				ans += "RGR";
    			R -= 2;
    			G--;
    			N -= 3;
    		}
    		else if ((G == 1 && R == 1 && N == 2) && (G > 1 && R >= 1)) {
    			ans += "RG";
    			R--;
    			G--;
    			N -= 2;
    		}
    		else {
    			cont = false;
    		}
    	}

    	while (cont && V > 0) {
    		if (V == 1 && Y >= 2) {
				ans += "YVY";
    			Y -= 2;
    			V--;
    			N -= 3;
    		}
    		else if ((V == 1 && Y == 1 && N == 2) || (V > 1 && Y >= 1)) {
    			ans += "YV";
    			Y--;
    			V--;
    			N -= 2;
    		}
    		else {
    			cont = false;
    		}
    	}

    	int start = ans.size();
    	if (start == 0) {
    		N--;
    		if (R >= Y && R >= B) {
    			ans += "R";
    			R--; 
    		}
    		else if (Y >= B) {
    			ans += "Y";
    			Y--;
    		}
    		else {
    			ans += "B";
    			B--;
    		}
    	}
    	while (cont && N--) {
    		if (last(ans) == 'R' && (Y > 0 || B > 0))  {
    			if (Y > B) {
    				ans += 'Y';
    				Y--;
    			}
    			else {
    				ans += 'B';
    				B--;
    			}
    		}
    		else if (last(ans) == 'Y' && (R > 0 || B > 0)) {
    			if (R > B) {
    				ans += 'R';
    				R--;
    			}
    			else {
    				ans += 'B';
    				B--;
    			}
    		}
    		else if (last(ans) == 'B' && (R > 0 || Y > 0)) {
    			if (R > Y) {
    				ans += 'R';
    				R--;
    			}
    			else {
    				ans += 'Y';
    				Y--;
    			}
    		}
    		else {
    			cont = false;
    		}
    	}

    	// check
    	if (cont) {
    		//cout << ans << " checking ans\n" ;
    		if (last(ans) == 'O' && ans[0] != 'B') cont = false;
	    	else if (last(ans) == 'G' && ans[0] != 'R') cont = false;
	    	else if (last(ans) == 'V' && ans[0] != 'Y') cont = false;

	    	else if (last(ans) == ans[0]) {
	    		for (int i = ans.size()-1; i > start; i--) {
	    			swap(ans[i], ans[i-1]);
	    			if (ans[i-1] != ans[i-2]) break;
	    		}

	    		for (int i = start-1; i < (int) ans.size()-1; i++) {
	    			if (ans[i] == ans[i+1]) {
	    				cont = false;
	    				break;
	    			}
	    		}
	    	}
    	}
    	if (cont) cout << ans << "\n";
    	else cout << "IMPOSSIBLE\n";
    }
}