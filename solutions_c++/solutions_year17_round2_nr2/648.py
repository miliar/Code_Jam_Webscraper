#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define oioi printf("oioi\n")
#define eoq cout << "eoq" << '\n'
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
typedef pair<double, double> dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
const int dx[] = {0 ,1,-1,0,1,-1,-1, 1};
const int dy[] = {-1,0,0, 1,1, 1,-1,-1};
const ll MOD = 0;
const ll N = 0;

//~ vector< vector< vector<int> > > dp[1020][3];

//~ set<pair<pos, pair<ult, pair<red, pair<yellow, blue> > > > > dp;
//~ map<pair<int, pair<int, pair<int, int> > >, int> dp;
//~ F, S.F, S.S.F, S.S.S.F, S.S.S.S
vector<vector<vector<vector<int> > > > dp;

string saida;
bool ok;
int n;
int solve(int ult, int red, int yell, int blue, string at){
	if(red==0 && yell==0 && blue==0){
		if(!ok){
			saida = at;
			ok = true;
		}
		return dp[ult][red][yell][blue] = 1; 
	}
	if(dp[ult][red][yell][blue]!=-1) return dp[ult][red][yell][blue];
	
	int ans = 0;
	if(!ok){
		
		if(ult==4){
			if(red){
				ans = ans || solve(0, red-1, yell, blue, at + 'R');
			}
			if(ans) return dp[ult][red][yell][blue] = 1;
			if(yell){
				ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
			}
			if(ans) return dp[ult][red][yell][blue] = 1;
			if(blue){
				ans = ans || solve(  2, red, yell, blue-1, at + 'B');
			}
			if(ans) return dp[ult][red][yell][blue] = 1;
		}else if(red+yell+blue==1){
			if(ult==0){
				if(at[0]=='R'){
					if(yell){
						ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
					if(blue){
						ans = ans || solve(  2, red, yell, blue-1, at + 'B');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}else if(at[0]=='Y'){
					if(blue){
						ans = ans || solve(  2, red, yell, blue-1, at + 'B');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}else if(at[0]=='B'){
					if(yell){
						ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}
			}else if(ult==1){//yell
				if(at[0]=='R'){
					if(blue){
						ans = ans || solve(  2, red, yell, blue-1, at + 'B');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}else if(at[0]=='Y'){
					if(red){
						ans = ans || solve(  0, red-1, yell, blue, at + 'R');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
					if(blue){
						ans = ans || solve(  2, red, yell, blue-1, at + 'B');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}else if(at[0]=='B'){
					if(red){
						ans = ans || solve(  0, red-1, yell, blue, at + 'R');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}
			}else if(ult==2){
				if(at[0]=='R'){
					if(yell){
						ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}else if(at[0]=='Y'){
					if(red){
						ans = ans || solve(  0, red-1, yell, blue, at + 'R');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}else if(at[0]=='B'){
					if(red){
						ans = ans || solve(  0, red-1, yell, blue, at + 'R');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
					if(yell){
						ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
					}
					if(ans) return dp[ult][red][yell][blue] = 1;
				}
				
			}
		}else{
			if(ult==0){
				if(yell){
					ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
				}
				if(ans) return dp[ult][red][yell][blue] = 1;
				if(blue){
					ans = ans || solve(  2, red, yell, blue-1, at + 'B');
				}
				if(ans) return dp[ult][red][yell][blue] = 1;
			}else if(ult==1){
				if(red){
					ans = ans || solve(  0, red-1, yell, blue, at + 'R');
				}
				if(ans) return dp[ult][red][yell][blue] = 1;
				if(blue){
					ans = ans || solve(  2, red, yell, blue-1, at + 'B');
				}
				if(ans) return dp[ult][red][yell][blue] = 1;
			}else if(ult==2){
				if(red){
					ans = ans || solve(  0, red-1, yell, blue, at + 'R');
				}
				if(ans) return dp[ult][red][yell][blue] = 1;
				if(yell){
					ans = ans || solve(  1, red, yell-1, blue, at + 'Y');
				}
				if(ans) return dp[ult][red][yell][blue] = 1;
			}
		}
		
		
	}
	
	return dp[ult][red][yell][blue] = ans;
}

int main () {
	
	int t, r, o, y, g, b, v;
	cin >> t;
	for(int tc = 1; tc<=t; tc++){
		ok = false;
		cin >> n >> r >> o >> y >> g >> b >> v;
		saida="";
		//~ dp.clear();
		dp.resize(5);
		for (int i = 0; i < 5; i++)
		{
			dp[i].resize(r+1);
			//~ oioi;
			for(int j=0; j<=r; j++){
				dp[i][j].resize(y+1);
				//~ oioi;
				for(int k=0; k<=y; k++){
					dp[i][j][k].resize(b+1);
					for(int kk=0; kk<=b; kk++){
						dp[i][j][k][kk] = -1;
						//~ cout << dp[i][j][k][kk] << endl;
					}
				}
			}
		}
		//~ oioi;
		
		cout << "Case #" << tc << ": ";
		if(solve(4, r, y, b, ""))
			cout << saida << "\n";
		else cout << "IMPOSSIBLE\n";
	}
	
	return 0;
}
