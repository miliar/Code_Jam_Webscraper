#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#define LL long long
using namespace std;
struct Line{
    LL len;
    LL num;
};
vector<Line> q;
void push(LL x,LL y){
    if(x==0) return;
    if(q[q.size()-1].len==x) {
            q[q.size()-1].num+=y;
    }
    else{Line p;p.len=x;p.num=y;
    q.push_back(p);
    }
}
int main(){
   //freopen("in.txt","r",stdin);
   //freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int t=1;t<=T;t++){
        LL n,k;
        scanf("%lld%lld",&n,&k);

        printf("Case #%d: ",t);
        q.clear();
        Line x;
        x.len=n;x.num=1;
        q.push_back(x);
        LL nl=n;
        LL ii=0;
        while(0<k){
            Line xx=q[ii];
          //  printf("%lld----%lld\n",xx.len,xx.num);
            k-=xx.num;
            nl=xx.len;
            push(nl/2,xx.num);push((nl-1)/2,xx.num);
            ii++;
        }
        printf("%lld %lld\n",nl/2,(nl-1)/2);
    }
    return 0;
}
