#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
struct node{
    long long sum,tag,siz;
}tree[400005];
void pushup(int rt){
    tree[rt].sum=tree[rt<<1].sum+tree[rt<<1|1].sum;
}
void pushdown(int rt){
    if(tree[rt].tag){
        tree[rt<<1].sum+=tree[rt<<1].siz*tree[rt].tag;
        tree[rt<<1|1].sum+=tree[rt<<1|1].siz*tree[rt].tag;
        tree[rt<<1].tag+=tree[rt].tag;
        tree[rt<<1|1].tag+=tree[rt].tag;
        tree[rt].tag=0;
    }
}
void build(int l,int r,int rt){
    tree[rt].tag=0;
    tree[rt].siz=r-l+1;
    if(l==r){
        scanf("%lld",&tree[rt].sum);
        return ;
    }
    int m=(l+r)>>1;
    build(lson);
    build(rson);
    pushup(rt);
    return ;
}
long long ans(int L,int R,int l,int r,int rt){
    if(L<=l&&r<=R){
        return tree[rt].sum;
    }
    pushdown(rt);
    int m=(l+r)>>1;
    long long ret=0;
    if(L<=m) ret+=ans(L,R,lson);
    if(R>m) ret+=ans(L,R,rson);
    return ret;
}
void Tag(int L,int R,int x,int l,int r,int rt){
    if(L<=l&&r<=R){
        tree[rt].sum+=tree[rt].siz*x;
        tree[rt].tag+=x;
        return ;
    }
    pushdown(rt);
    int m=(l+r)>>1;
    if(L<=m) Tag(L,R,x,lson);
    if(m<R) Tag(L,R,x,rson);
    pushup(rt);
}
int main(void){
    int i,j,n,m,L,R,X;
    char s[5];
    while(scanf("%d %d",&n,&m)!=EOF){
        build(1,n,1);
        for(i=0;i<m;i++){
            scanf("%s",s);
            if(s[0]=='Q') {
                scanf("%d %d",&L,&R);
                printf("%lld\n",ans(L,R,1,n,1));
            }
            else {
                scanf("%d %d %d",&L,&R,&X);
                Tag(L,R,X,1,n,1);
            }
        }
    }
}
