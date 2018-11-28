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
string solve(){
	string s;
	cin>>s;
	int N=s.size();
	if(N==1){
		return s;
	}
	if(string(N,'1')>s){
		return string(N-1,'9');
	}
	string ans;
	rep(i,N){
		if(s.substr(i,N-i)<string(N-i,s[i])){
			ans+=s[i]-1;
			ans+=string(N-1-i,'9');
			return ans;
		}else{
			ans+=s[i];
		}
	}
	return ans;
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		cout<<solve()<<endl;
	}
}
