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
#define ler freopen("ebola.in","r",stdin);freopen("ebola.out","w",stdout)
#define fastio ios::sync_with_stdio(0), cin.tie(0)
#define debug cout<<"!!?!!\n"
using namespace std; 
#define EPS 1e-9L
#define MOD 1000000007
#define INF 2000000000000000000LL
#define MAXN 100005

int t;

ld tempo(ld ini, ld vel, ld fim){
	if(ini>=fim) return 0;
	return (fim-ini)/vel;
}

int main(){
	cin >> t;
	
	ld d, n, ini, vel, menor;
	rep(caso,1,t+1){
		cin >> d >> n;
		menor= -1;
		
		rep(i,0,n){
			cin >> ini >> vel;
			menor= max(menor,tempo(ini,vel,d));
		}
		cout << setprecision(15) << fixed << "Case #" << caso << ": " << (d/menor) << endl;
	}
}














