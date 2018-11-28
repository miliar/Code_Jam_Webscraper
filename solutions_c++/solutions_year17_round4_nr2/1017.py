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
#define MAXN 1003
using namespace std;

int n, c, m, p[MAXN][MAXN], ansX, ansY;

int main(){
	int t; cin >> t;
	rep(caso,1,t+1){
		clr(p,0);
		cin >> n >> c >> m;
		rep(i,0,m){
			int a, b;
			cin >> a >> b;
			p[b][a]++;
		}

		int emp=0, cnt1=0, cnt2=0, sum=0;
		rep(i,1,n+1){
			sum= max(sum, p[1][i]+p[2][i]);
			cnt1+= p[1][i];
			cnt2+= p[2][i];
		}
		int maior= max(cnt1, cnt2);
		emp= max(0,sum-maior);
		
		if(sum <= maior){
			ansX= maior;
			ansY= 0;
		}
		else{
			if(p[1][1]+p[2][1]==sum){
				ansX= max(p[1][1]+p[2][1], maior);
				ansY= 0;				
			}
			else{
				ansX= maior;
				ansY= emp;
			}
		}
		cout << "Case #" << caso << ": "<< ansX << " " << ansY << endl;
	}
}








