#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

int T,n,r,o,y,g,b,v,x,z;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>n>>r>>o>>y>>g>>b>>v;
		cout<<"Case #"<<i+1<<": ";
		vector<pair<int,char> > vec;
		string s;
		vec.pb(mp(r,'R'));
		vec.pb(mp(y,'Y'));
		vec.pb(mp(b,'B'));
		sort(vec.rbegin(), vec.rend());
		x = vec[0].fi;
		z = vec[1].fi;
		char c1,c2,last;
		c1 = vec[0].sc;
		c2 = vec[1].sc;
		last = 0;
		while(z){
			if(last==0){
				s.pb(c1);
				x--;
			}
			else{
				s.pb(c2);
				z--;
			}
			last = !last;
		}
		z = vec[2].fi;
		c2 = vec[2].sc;
		while(x) s.pb(c1), x--;
		while(z>1){
			bool found = false;
			for(int i=0;i<s.size()-1;i++){
				if(s[i]==s[i+1]){
					s.insert(s.begin()+i+1, c2);
					z--;
					found = true;
					break;
				}
			}
			if(!found) break;
		}
		while(z>1){
			for(int i=0;i<s.size()-1;i++){
				if(s[i]!=c2 && s[i+1]!=c2){
					s.insert(s.begin()+i+1, c2);
					z--;
					break;
				}
			}
		}
		if(z) s.pb(c2);
		bool check = true;
		for(int i=0;i<s.size()-1;i++){
			if(s[i]==s[i+1]){
				check = false;
				break;
			}
		}
		if(s[0]==s[s.size()-1]) check = false;
		if(check) cout<<s<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
