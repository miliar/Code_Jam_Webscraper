#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define ZERO (1e-10)
#define INF (1<<29)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define DEB printf("DEB!\n");
#define D(X) cout<<"  "<<#X": "<<X<<endl;
#define EQ(A,B) (A+ZERO>B&&A-ZERO<B)
typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define IN(n) int n;scanf("%d",&n);
#define FOR(i, m, n) for (int i(m); i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)
#define FT(m, n) FOR(k, m, n)
#define aa first
#define bb second
void ga(int N,int *A){F(N)scanf("%d",A+i);}
#define MX (101)
int H,A,h,a,B,D;
struct st{
    int x,H,A,h,a,p;
    bool operator<(const st&r)const{
        return x^r.x?x<r.x:H^r.H?H<r.H:h^r.h?h<r.h:a^r.a?a<r.a:A<r.A;
    }
}w,v;
set<st> C;
deque<st> Q;
void bfs(){
    while(!Q.empty())Q.pop_front();
    C.insert({1,H,A,h,a,0});
    Q.PB({1,H,A,h,a,0});
    while(!Q.empty()){
        w=Q.front(),Q.pop_front();
//        printf("[%d]: %d/%d : %d/%d - %d\n",w.x,w.H,w.A,w.h,w.a,w.p);
        if(!w.x){
            v=w,v.H-=w.a,v.x^=1;
            if(w.H>w.a&&!C.count(v))
                Q.PB(v),C.insert(v);
        }else{
            if(w.h<=w.A){printf("%d\n",w.p+1);return;}
            v=w,v.h-=w.A,v.x^=1,++v.p;
            if(!C.count(v))Q.PB(v),C.insert(v);
            v=w,v.A+=B,v.x^=1,++v.p;
            if(!C.count(v))Q.PB(v),C.insert(v);
            v=w,v.H=H,v.x^=1,++v.p;
            if(!C.count(v))Q.PB(v),C.insert(v);
            v=w,v.a=max(v.a-D,0),v.x^=1,++v.p;
            if(!C.count(v))Q.PB(v),C.insert(v);
        }
    }
    puts("IMPOSSIBLE");
}
int main(void){
    IN(_)F(_)printf("Case #%d: ",i+1),scanf("%d%d%d%d%d%d",&H,&A,&h,&a,&B,&D),C.clear(),bfs();
    return 0;
}
