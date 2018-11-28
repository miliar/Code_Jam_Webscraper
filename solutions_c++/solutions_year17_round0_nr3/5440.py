#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;
typedef long long LL;
int T,n,k;
map<LL,LL> M;
int main(){
	//freopen("C-small-2-attempt0.in","r",stdin);
	//freopen("C-small-2-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        printf("Case #%d: ",cas);
        scanf("%d%d",&n,&k);
        M.clear(); 
        priority_queue<LL> Q;
        Q.push(n); M[n]=1;
        for(;;){
            LL u=Q.top();Q.pop();
            if(M[u]==0)continue;
            LL x=u/2,y=(u-1)/2;
            if(M[u]>=k){printf("%lld %lld\n",x,y);break;}
            if(M[x]==0)Q.push(x);
            if(M[y]==0)Q.push(y);
            M[x]+=M[u];M[y]+=M[u];
			k-=M[u];M[u]=0;
        }
    }return 0;
}
