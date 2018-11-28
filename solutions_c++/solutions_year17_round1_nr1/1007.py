#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i=(a); i<(b); i++)
#define pb push_back
#define mk make_pair
#define debug(x) cout<<__LINE__<<": "<<#x<<" = "<<x<<endl;
#define all(c) (c).begin(), (c).end()
#define F first
#define S second
#define UNIQUE(c) sort(all(c)); (c).resize(unique(all(c))-c.begin());
#define pi 3.1415926535897932384626433832795028841971

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

inline int cmp(double x, double y = 0, double tol = EPS){
	return ((x <= y+tol) ? (x+tol < y) ? -1:0:1); }


string int2str(int x){ stringstream ss; string str; ss << x; ss >> str;  return str; }
int str2int(string str){ stringstream ss; int x; ss << str; ss >> x;  return x; }

int R, C;
char m[33][33];

void goR(int i, int j){
	char ch = m[i][j];
	while (j+1 < C && m[i][j+1] == '?'){
		m[i][j+1] = ch;
		j++;
	}
}

void goL(int i, int j){
	char ch = m[i][j];
	while (j-1 >=0 && m[i][j-1] == '?'){
		m[i][j-1] = ch;
		j--;
	}
}


void goU(int i, int j){
	char ch = m[i][j];
	while (i-1 >= 0 && m[i-1][j] == '?'){
		m[i-1][j] = ch;
		i--;
	}
}


void goD(int i, int j){
	char ch = m[i][j];
	while (i+1 < R && m[i+1][j] == '?'){
		m[i+1][j] = ch;
		i++;
	}
}

void showM(){
	rep(i,0,R){
		rep(j,0,C)
			printf("%c", m[i][j]);
		printf("\n");
	}
}

void solve(){
	rep(i,0,R) rep(j,0,C){
		if (m[i][j] != '?'){
			goR(i,j);
			goL(i,j);	
		}
	}
	// so existe linhas em branco se inicialmente estavam em branco
	rep(i,0,R) rep(j,0,C){
		if (m[i][j] != '?'){
			goU(i,j);
			goD(i,j);	
		}
	}
}

int main(){

	int tn; cin >> tn;
	rep(t,0,tn){
		printf("Case #%d:\n", (t+1));
		
		cin >> R >> C;
		rep(i,0,R){
			scanf("%s", m[i]);
		}
		solve();
		showM();
	}
	return 0;
}









