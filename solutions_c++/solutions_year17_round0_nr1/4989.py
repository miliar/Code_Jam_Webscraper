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

int t;
int main(){
	cin >> t;
	
	for(int caso=1; caso<=t; caso++){
		string s; int k;
		cin >> s >> k;
		int ans=0;
		rep(i,0,sz(s)-k+1){
			if(s[i]=='-'){
				ans++;	
				rep(j,i,i+k) s[j]=(s[j]=='+'?'-':'+');
			}
		}
		
		rep(i,sz(s)-k,sz(s)) if(s[i]=='-') ans=-1;
		if(ans!=-1)	cout << "Case #" << caso << ": " << ans << endl;
		if(ans==-1)	cout << "Case #" << caso << ": IMPOSSIBLE\n";
	}
}












