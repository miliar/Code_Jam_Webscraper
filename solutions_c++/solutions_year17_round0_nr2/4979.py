#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
#define ld long double
#define sz(a) ((int)(a).size())
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define pii pair<int,int>
#define pdd pair<ld,ld> 
#define rep(i,a,b) for(int i=a; i<b; i++)
#define dec(i,a,b) for(int i=a; i>=b; i--)
#define ler freopen("inspection.in","r",stdin);freopen("inspection.out","w",stdout)
#define fastio ios::sync_with_stdio(0), cin.tie(0)
#define debug cout<<"!!?!!\n"
using namespace std; 
#define EPS 1e-9
#define MOD 1000000007
#define INF 1e9
#define MAXN 11000000

string s;
int dp[22][11][2];
int A[22][11][2], B[22][11][2];

int solve(int p, int x, int r){
	if(dp[p][x][r]!=-1) return dp[p][x][r];
	if(p+1==sz(s) && x==0) return false;
	if(p==sz(s)) return true;
	if(r==false && x>s[p]) return false;
	//cout << p << " " << x << " " << r << endl;
	int ok=false;

	for(int i=9; i>=x; i--){
		if(solve(p+1,i,r|(x!=s[p]))){
			A[p][x][r]= i;
			B[p][x][r]= r|(x!=s[p]);
			ok=true;
			break;
		}
	}
	return dp[p][x][r]=ok;
}

void gera(int p, int x, int lead){
	if(p==sz(s)) return;
	if(!lead || x!=0) cout << x;
	else if(lead && x!=0) cout << x;
	gera(p+1,A[p][x][lead],B[p][x][lead]);
}

int main(){
	int t;
	cin >> t;
	
	for(int caso=1; caso<=t; caso++){
		cout << "Case #" << caso << ": ";
		cin >> s;
		rep(i,0,sz(s)) s[i]-='0';
		
		clr(dp,-1);
		clr(A,-1); 
		clr(B,-1);
		for(int i=s[0]; i>=0; i--){
			if(solve(0,i,i!=s[0])){
				gera(0,i,i!=s[0]);
				break;
			}
		}
		cout << "\n";
	}
}









