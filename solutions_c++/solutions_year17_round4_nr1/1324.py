#include <bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(0);

	int tc=0,t;
	cin >> t;
	for(tc=0;tc<t;++tc){
		int n,p,x,i;
		cin >> n >> p;
		vector<int>v[p];
		for(i=0;i<n;++i){
			cin >> x;
			v[x%p].emplace_back(x);
		}
		vector<int>a;
		if(p==2){
			for(i=0;i<int(v[0].size());++i){
				a.emplace_back(v[0][i]);
			}
			for(i=0;i<int(v[1].size());++i){
				a.emplace_back(v[1][i]);
			}
		}
		if(p==3){
			for(i=0;i<int(v[0].size());++i){
				a.emplace_back(v[0][i]);
			}
			for(i=0;i<min<int>(v[1].size(),v[2].size());++i){
				a.emplace_back(v[1][i]);
				a.emplace_back(v[2][i]);
			}
			for(;i<int(v[1].size());++i){
				a.emplace_back(v[1][i]);
			}
			for(;i<int(v[2].size());++i){
				a.emplace_back(v[2][i]);
			}
		}
		if(p==4){
			for(i=0;i<int(v[0].size());++i){
				a.emplace_back(v[0][i]);
			}
			for(i=0;i<min<int>(v[1].size(),v[3].size());++i){
				a.emplace_back(v[1][i]);
				a.emplace_back(v[3][i]);
			}
			for(i=0;i+1<v[2].size();i+=2){
				a.emplace_back(v[2][i]);
				a.emplace_back(v[2][i+1]);
			}
			if(v[2].size()&1){
				a.emplace_back(v[2].back());
			}
			for(i=min<int>(v[1].size(),v[3].size());i<int(v[1].size());++i){
				a.emplace_back(v[1][i]);
			}
			for(i=min<int>(v[1].size(),v[3].size());i<int(v[3].size());++i){
				a.emplace_back(v[3][i]);
			}
		}
		assert(int(a.size())==n);
		int ofs=0, nw=0;
		for(i=0;i<n;++i){
			if(ofs==0) ++nw;
			a[i]+=ofs;
			ofs=a[i]%p;
		}
		cout << "Case #" << tc+1 << ": ";
		cout << nw << '\n';
		cerr << "Solved " << tc+1 << '\n';
	}
	return 0;
}