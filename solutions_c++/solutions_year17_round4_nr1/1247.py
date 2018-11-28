#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
typedef long long ll;

int T,n,k,res,cs,v[5];

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.ou","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.ou","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&k);
		res=0;
		for(int i=0; i<k; ++i) v[i]=0;
		for(int i=0,x; i<n; ++i){
			scanf("%d",&x);
			++v[(k-x%k)%k];
		}
		if(k==2){
			res=v[0]+(v[1]+1)/2;
		}else if(k==3){
			res=v[0];
			int a=min(v[1],v[2]);
			res+=a;
			v[1]-=a;
			v[2]-=a;
			res+=v[1]/3;
			v[1]%=3;
			res+=v[2]/3;
			v[2]%=3;
			if(v[1] || v[2])++res;
		}else{
			res=v[0];
			int a=min(v[1],v[3]);
			res+=a;
			v[1]-=a;
			v[3]-=a;
			a=min(v[3]/2,v[2]);
			res+=a;
			v[3]-=a*2;
			v[2]-=a;
			a=min(v[1]/2,v[2]);
			res+=a;
			v[1]-=a*2;
			v[2]-=a;
			res+=v[1]/4;
			v[1]%=4;
			res+=v[3]/4;
			v[3]%=4;
			res+=v[2]/2;
			v[2]%=2;
			if(v[1] || v[2] || v[3]) ++res;
		}
		printf("Case #%d: %d\n",++cs,res);
	}
}