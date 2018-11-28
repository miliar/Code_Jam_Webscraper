#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<time.h>
#include<assert.h>
#include<iostream>
using namespace std;
typedef long long LL;
typedef pair<LL,LL>pi;
void zl(vector<pi>&tmp){
	vector<pi>nxt;
	sort(tmp.begin(),tmp.end());
	for(int i=0;i<tmp.size();i++){
		if(nxt.size()&&nxt.back().first==tmp[i].first){
			nxt.back().second+=tmp[i].second;
		}
		else nxt.push_back(tmp[i]);
	}
	reverse(nxt.begin(),nxt.end());
	swap(tmp,nxt);
}
int main(){
	freopen("C-large.in.txt","r",stdin);
	freopen("C-large.out.txt","w",stdout);
	int _;scanf("%d",&_);
	int cas=1;
	while(_--){
		LL n,k;
		cin>>n>>k;
		LL ansl,ansr;
		vector<pi>V;
		V.push_back(pi(n,1));
		while(1){
			vector<pi>nxt;
			bool flag=0;
			for(int i=0;i<V.size();i++){
				LL x=V[i].first,y=V[i].second;
				if(k<=y){
					ansl=x/2,ansr=(x-1)/2;
					flag=1;
					break;
				}
				else {
					k-=y;
					nxt.push_back(pi(x/2,y));
					nxt.push_back(pi((x-1)/2,y));
				}
			}
			if(flag)break;	
			zl(nxt);
			swap(nxt,V);
		}
		printf("Case #%d: ",cas++);
		printf("%lld %lld\n",ansl,ansr);
	}
	return 0;
}
