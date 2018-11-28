#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

LL T;
string s;
vector<LL> v;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		cin>>s;
		v.clear();
		bool check;
		for(int i=0;i<s.size();i++) v.pb(s[i]-'0');
		while(true){
			check = true;
			for(int i=v.size()-1;i>0;i--){
				if(v[i-1]>v[i]){
					for(int j=i-1;j>=0;j--){
						v[j]--;
						if(j==0 && v[j]==0){
							v.erase(v.begin());
							for(int k=0;k<v.size();k++) v[k] = 9;
						}
						if(v[j]!=-1){
							for(int k=j+1;k<v.size();k++) v[k] = 9;
							break;
						}
					}
					check = false;
					break;
				}
			}
			if(check) break;
		}
		LL ans = 0;
		for(int i=0;i<v.size();i++){
			ans *= 10;
			ans += v[i];
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}
