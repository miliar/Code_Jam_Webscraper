#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define F first
#define S second
#define mp make_pair
using namespace std;
typedef long long ll;
int cas,t;
long long n,ans,lef,rig,l,k;

int main(){
#ifdef AKAISORA
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		scanf("%I64d %I64d",&n,&k);
		printf("Case #%d: ",t);
		
		map<ll,ll> M;
		map<ll,ll>::iterator it,tmp;
		M.insert(mp(n,1));
		while(k>0){
			it=M.end();
			it--;
			lef=(it->F-1)/2;
			rig=(it->F)/2;
			if(lef>0){
				tmp=M.find(lef);
				if(tmp==M.end()){
					M.insert(mp(lef,it->S));
				}
				else{
					tmp->S+=it->S;
				}
			}
			if(rig>0){
				tmp=M.find(rig);
				if(tmp==M.end()){
					M.insert(mp(rig,it->S));
				}
				else{
					tmp->S+=it->S;
				}				
			}
			k-=it->S;
			M.erase(it);
		}
		printf("%I64d %I64d\n",rig,lef);
	}
	return 0;
}