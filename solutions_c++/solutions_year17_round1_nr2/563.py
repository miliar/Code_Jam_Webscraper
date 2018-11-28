#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int n,p;cin>>n>>p;
		vector<int> grams(n);
		for(int& x: grams) cin>>x;
		vector<vector<pair<int,int>>> packages(n);
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				int x;cin>>x;
				double val=((double)x)/grams[i];
				int m=floor(val/0.9), mm=ceil(val/1.1);
				if(m>0 && mm<=m) packages[i].push_back({mm,m});
			}
			sort(packages[i].begin(), packages[i].end(), [](pair<int,int> l, pair<int,int> r){
				if(l.first==r.first) return l.second<r.second;
				return l.first<r.first;
			});
		}
		int count=0;
		bool done=false;
		for(auto& x: packages){
			if(x.empty()){
				done=true;
				break;
			}
		}
		if(done){
			cout<<"Case #"<<t<<": 0"<<endl;
			continue;
		}
		vector<int> index(n, 0);
		while(true){
			bool rerun=false;
			int minValmaxVal=-1;
			int minVal=-1;
			auto mm=packages[0][index[0]];
			for(int i=1;i<n;i++){
				mm.first=max(mm.first, packages[i][index[i]].first);
				mm.second=min(mm.second, packages[i][index[i]].second);
			}
			if(mm.first<=mm.second){
				count++;
				for(int i=0;i<n;i++){
					index[i]++;
					if(index[i]>=packages[i].size()){
						done=true;
						break;
					}
				}
				if(done) break;
				else continue;
			}
			for(int i=0;i<n;i++){
				while(packages[i][index[i]].second<mm.first){
					index[i]++;
					if(index[i]>=packages[i].size()){
						done=true;
						break;
					}
				}
				if(done) break;
			}
			if(done) break;
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}