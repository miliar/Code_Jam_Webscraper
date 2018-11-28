#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

int T,n;
string s;
vector<int> v;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>s>>n;
		v.clear();
		int ans = 0;
		for(int j=0;j<s.size();j++){
			if(s[j]=='+') v.pb(1);
			else v.pb(0);
		}
		while(true){
			bool check=true;
			for(int j=0;j<v.size();j++){
				if(v[j]==0){
					if(j+n-1>=v.size()){
						ans = -1;
						break;
					}
					for(int k=0;k<n;k++){
						v[j+k] = !v[j+k];
					}
					ans++;
					check = false;
					break;
				}
			}
			if(ans==-1) break;
//			for(int j=0;j<v.size();j++) cout<<v[j]<<" ";cout<<endl;
			if(check) break;
		}
		if(ans==-1) printf("Case #%d: IMPOSSIBLE\n", i);
		else printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
