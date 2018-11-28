#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
typedef pair<int,int> pii;
inline pii dispose(int x){
	if(x&1)return pii(x>>1,x>>1);
	else return pii((x>>1)-1,x>>1);
}
int main(){
	freopen("C-small-2-attempt0.bin","r",stdin);
	freopen("C.out","w",stdout);
	int T,n,k,cnt;
	cin>>T;
	for(int t(1);t<=T;t++){
		cin>>n>>k;
		cnt=0;
		vector<int> v[2];
		v[0].clear();v[1].clear();
		v[0].push_back(n);
		int now=0;
		for(;;){
			int tmp=cnt;
			cnt+=v[now].size();
			if(cnt>=k){
				sort(v[now].begin(),v[now].end(),greater<int>());
				printf("Case #%d: %d %d\n",t,dispose(v[now][k-tmp-1]).second,dispose(v[now][k-tmp-1]).first);
				break;
			}
			else{
				v[now^1].clear();
				for(int i(0);i<v[now].size();i++){
					if(v[now][i]==0||v[now][i]==1)continue;
					pii tt=dispose(v[now][i]);
					v[now^1].push_back(tt.first);
					v[now^1].push_back(tt.second);
				}
			}
			now^=1;
		}
	}
	return 0;
}
