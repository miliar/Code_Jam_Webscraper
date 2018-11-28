#include <bits/stdc++.h>

using namespace std;

int r, c;
string s[50];
string re[50];
set<char> p;
string un;
int vis[500];
bool done = false;

bool chk() {
	memset(vis, 0, sizeof vis);
	bool res = true;
	for(int i=0; i<r && res; i++ ) {
		for(int j=0; j<c && res; j++ ) {
			if(s[i][j] != '?' && s[i][j] != re[i][j]) {
				res = false;
				continue;
			}
			if(i == 0 && j == 0) {
				vis[re[i][j]] = 1;
				continue;
			}
			if(i == 0) {
				if(re[i][j] == re[i][j-1]) {
					vis[re[i][j]] = 1;
					continue;
				}
				if(vis[re[i][j]]) {
					res = false;
				} else {
					vis[re[i][j]] = 1;
				}
				continue;
			}
			if(j == 0) {
				if(re[i][j] == re[i-1][j]) {
					vis[re[i][j]] = 1;
					continue;
				}
				if(vis[re[i][j]]) {
					res = false;
				} else {
					vis[re[i][j]] = 1;
				}
				continue;
			}
			if(re[i][j] == re[i-1][j-1]) {
				if(re[i][j] != re[i-1][j]) {
					vis[re[i][j]] = 1;
					res = false;
					continue;
				}
				if(re[i][j] != re[i][j-1]) {
					vis[re[i][j]] = 1;
					res = false;
					continue;
				}
				continue;
			}
			if(re[i-1][j-1] == re[i-1][j] && re[i-1][j-1] == re[i][j-1]) {
				res = false;
				continue;
			}
			if(re[i][j] == re[i-1][j]) {
				vis[re[i][j]] = 1;
				continue;
			}
			if(re[i][j] == re[i][j-1]) {
				vis[re[i][j]] = 1;
				continue;
			}
			if(vis[re[i][j]]) {
				res = false;
			} else {
				vis[re[i][j]] = 1;
			}
			continue;
		}
	}
	// cout << "return : " << res << endl;
	return res;
}

void pr() {
	cout << endl;
	for(int i=0; i<r; i++) {
		for(int j=0; j<c; j++ ) {
			cout << re[i][j];
		}
		cout << endl;
	}
}

bool fill(int x, int y) {
	if (done) {
		return true;
	}
	if(x == r && y == c) {
		if(chk()) {
			pr();			
			done = true;
		}
		return false;
	}
	if(y == c) {
		return fill(x+1, 0);
	}
	if(s[x][y] != '?') {
		// cout << "Here : " << x << " " << y << endl;
		re[x][y] = s[x][y];
		// cout << "bla : " << re[0][0] << endl;
		return fill(x, y+1);
	}
	bool res = false;
	set<char>::iterator it;
	for (it = p.begin(); it != p.end(); it++) {
		char val = *(it);
		re[x][y] = val;
		res |= fill(x, y+1);
	}
	// for(int i=0; i<un.size(); i++ ) {
	// 	char val = un[i];
	// 	// cout << "x, y : " << x << " " << y << " " << re[0][0] << endl;
	// 	re[x][y] = val;
	// 	// cout << "x, y : " << x << " " << y << " " << re[0][0] << endl;
	// 	res |= fill(x, y+1);	
	// } 
	return res;
}

void solve() {
	done = false;
	p.clear();
	un = "";
    cin >> r >> c;
    for(int i=0; i<r; i++ ) {
    	cin >> s[i];
    	re[i] = s[i];
    }
    for(int i=0; i<r; i++ ) {
    	for(int j=0; j<c; j++ ) {
    		if(s[i][j] == '?') continue;
    		p.insert(s[i][j]);
    		// cout << s[i][j] << " " << endl;
    		un += (char) s[i][j];
    	}
    }
    // cout << "Size of set : " << p.size() << endl;
    fill(0, 0);
}

int main() {
    int ite;
    cin >> ite;
    for(int TT = 1; TT <= ite; TT++) {
        cout << "Case #" << TT <<": ";
        solve();
    }
    return 0;
}

