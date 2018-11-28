#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
template<class S,class T> ostream& operator<<(ostream& o,const pair<S,T> &p){return o<<"("<<p.fs<<","<<p.sc<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T> &vc){o<<"sz = "<<vc.size()<<endl<<"[";for(const T& v:vc) o<<v<<",";o<<"]";return o;}

int H,W;
string s[25];
void solve(){
	cin>>H>>W;
	rep(i,H) cin>>s[i];
	bool has[25]={};
	rep(i,H){
		rep(j,W) if(s[i][j]!='?') has[i]=1;
	}
	rep(i,H) if(has[i]){
		char c = '.';
		rep(j,W){
			if(s[i][j]!='?'){
				c=s[i][j];
				break;
			}
		}
		rep(x,W){
			if(s[i][x]!='?'){
				c=s[i][x];
			}
			s[i][x]=c;
		}
	}
	rep1(i,H-1) if(!has[i] && has[i-1]){
		rep(j,W) s[i][j]=s[i-1][j];
		has[i]=1;
	}
	for(int i=H-2;i>=0;i--) if(!has[i] && has[i+1]){
		rep(j,W) s[i][j]=s[i+1][j];
		has[i]=1;
	}
	rep(i,H) cout<<s[i]<<endl;
}

int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d:\n",t);
		solve();
	}
}
