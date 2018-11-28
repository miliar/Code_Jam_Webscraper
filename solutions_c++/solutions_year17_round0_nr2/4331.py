#include <bits/stdc++.h>
#define fore(i,a,n) for(int i=a,qwer=n;i<qwer;i++)
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
string s;
vector<string> w;
bool ok(string t) {
	char mx=t[0];
	fore(i,0,t.size()) {
		if(mx>t[i]) return 0;
		mx=max(mx,t[i]);
	}
	return t<=s;
}
int main() {
	int tn;
	cin>>tn;
	fore(tc,0,tn) {
		w.clear();
		cin>>s;
		string t=s;
		for(int i=s.size()-1;i>=0;i--) {
			if(ok(s)) {w.pb(s); break;}
			if(s[i]=='0') continue;
			if(i==0&&s[i]=='1') continue;
			t=s;
			t[i]=s[i]-1;
			fore(j,i+1,s.size()) t[j]='9';
			if(ok(t)) {w.pb(t); break;}
		}
		ll ans=0;
		if(w.size()) {
			s=w[0];
			fore(i,0,s.size()) {ans*=10LL; ans+= s[i]-'0';}
		} else fore(i,0,s.size()-1) {ans*=10LL; ans+=9LL;}
		printf("Case #%d: %lld\n",tc+1,ans);
	}
	return 0;
}
