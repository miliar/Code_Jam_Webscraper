#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define DINF 1e+12
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) if(1) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " " << y << "\n";
#define all(S) (S).begin(), (S).end()
#define MAXV 1005
#define F first
#define S second
#define EPS 1e-9
#define mp make_pair


using namespace std;

typedef long long ll;
typedef pair < int, int >  ii;

int tc, L, C;
char m[28][28];


int main(){
	
	// freopen("alarge.in", "r", stdin);
	// freopen("out1.txt", "w", stdout);
	
	int tt=1;
	
	cin >> tc;
	
	while(tc--){
		
		cin >> L >> C;
		vector<ii> v;
		
		rep(i, 0, L)
		rep(j, 0, C){
			scanf(" %c", &m[i][j]);
			v.pb(ii(i, j));
		}
		
		rep(k, 0, v.size()){
			
			int x = v[k].F;
			int y = v[k].S;
			char val = m[x][y];
			
			for(int j=y-1; j>=0; j--){
				if(m[x][j] == '?') m[x][j] = val;
				else break;
			}
			
			for(int j=y+1; j<C; j++){
				if(m[x][j] == '?') m[x][j] = val;
				else break;
			}
			
		}
		
		int linha = -1;
		rep(i, 0, L){
			if(m[i][0] != '?'){
				linha = i;
				break;
			}
		}
		
		rep(i, linha+1, L){ // p baixo da primeira
			if(m[i][0] == '?'){
				rep(j, 0, C){
					m[i][j] = m[i-1][j];
				}
			}
		}
		
		for(int i=linha-1; i>=0; i--)
			if(m[i][0] == '?'){
				rep(j, 0, C){
					m[i][j] = m[i+1][j];
				}
			}
		
		printf("Case #%d:\n", tt++);
		rep(i, 0, L){
			rep(j, 0, C){
				cout << m[i][j];
			}
			cout << endl;
		}
		
		
	}

	return 0;
}











