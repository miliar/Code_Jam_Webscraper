#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		LL N,K;
		cin>>N>>K;
		map<LL,LL> cnt[2];
		cnt[0][N]=1;
		LL x=0;
		int idx=0;
		LL Max=-1,Min=-1;
		while(1) {
			cnt[idx^1].clear();
			for(auto itr=cnt[idx].rbegin();itr!=cnt[idx].rend();itr++) {
				LL l=(itr->first-1)/2,r=itr->first/2;
				if(x+itr->second<=K-1) {
					x+=itr->second;
					if(l>0) cnt[idx^1][l]+=itr->second;
					if(r>0) cnt[idx^1][r]+=itr->second;
				}else {
					Max=r;
					Min=l;
					break;
				}
			}
			if(Max!=-1) break;
			idx^=1;
		}
		cout<<"Case #"<<t<<": "<<Max<<" "<<Min<<endl;
	}
}
