#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MS(a) memset(a,0,sizeof(a))
#define MP make_pair
#define PB push_back
const int INF = 0x3f3f3f3f;
const ll INFLL = 0x3f3f3f3f3f3f3f3fLL;
inline ll read(){
    ll x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
//////////////////////////////////////////////////////////////////////////
const int maxn = 1e5+10;

int mp[10],f[300],f_s[300];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	string s;
	int T = read();
	for(int cas=1; cas<=T; cas++){
		cin >> s; 
		MS(f); MS(mp);
		int len = s.size();
		
		int t=0;
		for(int i=0; i<len; i++){
			for(int t=s[i]-'0'+1; t<=9; t++){
				if(mp[t]) {f[i] = 1; break;}
			}
			if(f[i]) {t=i;break;}
			mp[s[i]-'0'] = 1;
		}
		// cout <<t  << endl;
		if(t == 0) {cout << "Case #" << cas << ": " << s << endl; continue;}
		t--;
		for(int i=t+1; i<len; i++){
			s[i] = '9';
		}
		while(t>0 && s[t]==0) { s[t]='9'; t--;}
		// cout << s[t+1] << " " << t << endl;
		s[t] = s[t]-1;
		// cout << s[t] << endl;
		int tt=t;
		while(1){
			if(t==0) break;
			bool k=1;
			tt = t;
			for(int i=0; i<tt; i++){
				if(s[tt] < s[i]){
					k = 0;
					tt = i;
					break;
				}
			}	
			// cout << t << " " << tt << " " << s[tt] << endl;
			if(k) break;
			for(int i=tt+1; i<=t; i++) s[i]='9';
				// cout << s << endl;
			t = tt;
			while(t>0 && s[t]=='0') {  s[t]='9';t--;}
			s[t] = s[t]-1;
		}


		cout << "Case #" << cas << ": ";
		if(s[0] == '0') {for(int i=1; i<len; i++) {if(s[i]==0) continue; cout<<s[i];} puts("");}
		else cout << s << endl;
	}


    return 0;
}