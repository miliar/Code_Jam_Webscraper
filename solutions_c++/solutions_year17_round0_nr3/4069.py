#include "bits/stdc++.h"
#define point pair<int,int>
#define state pair<int,point>
#define f first
#define s second
using namespace std;
class compare{
    public: bool operator ()(state x,state y){
        return (x.f<y.f)||(x.f==y.f&&x.s.f>y.s.f);
    };
};
int test,n,k,x,y;
state p;
bool check;
int main(){
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("C-small-2-attempt1.out","w",stdout);
    scanf("%d",&test);
    for(int l=1;l<=test;l++){
        priority_queue<state,vector<state>,compare> q;
        check=false;
        scanf("%d %d",&n,&k);
        q.push(state(n,point(1,n)));
        for(int i=1;i<=k;i++){
            p=q.top(),q.pop();
            if(p.f==1){
                printf("Case #%d: 0 0\n",l),check=true; break;
            }
            p.f--,x=((p.f&1==1)? ((p.f>>1)+1):(p.f>>1)),y=p.f-x;
            if(x>0) q.push(state(x,point(p.s.f,p.s.f+x)));
            if(y>0) q.push(state(y,point(p.s.f+2,p.s.s)));
        }
        if(!check) printf("Case #%d: %d %d\n",l,max(x,y),min(x,y));
    }
}
