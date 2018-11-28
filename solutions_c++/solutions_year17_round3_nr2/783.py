#include <bits/stdc++.h>

using namespace std;
#define int long long 
#define MOD 1000000007

vector<pair<int,pair<int,int> > > v;

signed main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t=1;t<=tt;t++){
		cout << "Case #" << t << ": ";
		int c,j;
		cin >> c >> j;
		int x,y;
		int a = 0,b = 0;
		v.clear();
		for(int i=0;i<c;i++){
			cin >> x >> y;
			v.push_back({x,{y,0}});
			a += y-x;
		}
		for(int i=0;i<j;i++){
			cin >> x >> y;
			v.push_back({x,{y,1}});
			b += y-x;
		}
		sort(v.begin(),v.end());
		int res = 0;
		if(v[0].second.second != v[c+j-1].second.second) res = 1;
		vector<int> aa,bb;
		int n = c+j;
		//for(int i=0;i<n;i++) cout << v[i].first << " " << v[i].second.first << endl;
		for(int i=0;i<n-1;i++){
			//cout << v[i].second.second << " " << v[i+1].second.second << endl;
			if(v[i].second.second != v[i+1].second.second) res += 1;
			else{
				//cout << "HERE" << endl;
				if(v[i].second.second == 0){
					a += v[i+1].first - v[i].second.first;
					//cout << v[i+1].first << " " << v[i].second.first << endl;
					aa.push_back(v[i+1].first - v[i].second.first);
				}
				else{
					b += v[i+1].first - v[i].second.first;
					bb.push_back(v[i+1].first - v[i].second.first);
				}
			}
		}
		if(v[0].second.second == v[n-1].second.second){
			int temp = v[0].first + 1440 - v[n-1].second.first;
			if(v[0].second.second == 0){
				a += temp;
				aa.push_back(temp);
			}
			else{
				b += temp;
				bb.push_back(temp);
			}
		}
		//cout << a << " " << b << " " << res << endl;
		if( a <= 720 && b<= 720){
			cout << res << "\n";
		}
		else{
			if(a > 720){
				//cout << a << endl;
				//for(int i=0;i<aa.size();i++) cout << aa[i] << endl;
				int k = a-720;
				sort(aa.begin(),aa.end());
				reverse(aa.begin(),aa.end());
				for(int i=0;i<aa.size();i++){
					res+=2;
					k -= aa[i];
					if(k <= 0) break;
				}
			}
			else{
				int k = b-720;
				sort(bb.begin(),bb.end());
				reverse(bb.begin(),bb.end());
				for(int i=0;i<bb.size();i++){
					res+=2;
					k -= bb[i];
					if(k <= 0) break;
				}
			}
			cout << res << "\n";
		}

	}
	return 0;
}