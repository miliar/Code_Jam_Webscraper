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
#define N 100007
using namespace std;
#define MAXN 102

ll dp[MAXN][MAXN][MAXN], n, t, p;

ll solve(int a, int b, int c){
	if(a+b+c==0) return 0;
	if(dp[a][b][c]!=-1) return dp[a][b][c];
	
	ll ans=0;
	if(a>0) ans= max(ans, solve(a-1,b,c) + ((b+c*2)%3==0));
	if(b>0) ans= max(ans, solve(a,b-1,c) + ((b-1 + c*2)%3==0));
	if(c>0) ans= max(ans, solve(a,b,c-1) + ((b + (c-1)*2)%3==0));
	return dp[a][b][c]= ans;
}

int main(){
	clr(dp,-1);
	cin >> t;
	
	rep(caso,1,t+1){
		cin >> n >> p;
		
		int a=0, b=0, c=0;
		rep(i,0,n){
			int x; cin >> x;
			if(x%p==0) a++;
			else if(x%p==1) b++;
			else if(x%p==2) c++;
		}
		
		if(p==3) cout << "Case #" << caso << ": " <<  solve(a,b,c) << endl;
		else{
			cout << "Case #" << caso << ": " <<  a+(b+1)/2 << endl;
		}
	}
}










