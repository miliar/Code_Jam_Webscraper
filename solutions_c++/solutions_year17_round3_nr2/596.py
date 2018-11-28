#include <stdio.h>
#include <algorithm>
#define N 100
using namespace std;

struct emp{
    int a,b,p,q,s,e,t;
};
emp E,a[N+5],b[N+5],p[2*N+5],q[2*N+5];

int ans;
bool sort_cmp(emp x,emp y){
    return x.s<y.s;
}
bool sort_cmp1(emp x,emp y){
    return x.p>y.p;
}
int solve(int tt){
    int i,x,y,s,e;
    emp t,r;

    t.t=t.p=r.t=r.p=0;

    sort(a,a+E.a,sort_cmp);
    sort(b,b+E.b,sort_cmp);
    sort(p,p+E.p,sort_cmp);

    s=e=x=y=0;
    E.q=0;
    ans=0;

    if(!p[0].t)
        s=e=p[0].s;

    t.t=p[0].t;
    t.p=p[0].s;

    for(i=0;i<E.p-1;i++){
        if(!p[i].t){
            s+=p[i].e-p[i].s;
            e+=p[i].e-p[i].s;
        }
        if(p[i].t^p[i+1].t){
            e+=p[i+1].s-p[i].e;
            ans++;
        }else{
            s+=(p[i+1].s-p[i].e)*(1-p[i].t);
            e+=(p[i+1].s-p[i].e)*(1-p[i].t);
            q[E.q].t=p[i].t;
            q[E.q++].p=(p[i+1].s-p[i].e);
        }
    }
    if(!p[i].t){
        s+=p[i].e-p[i].s;
        e+=p[i].e-p[i].s;
    }
    if(!p[i].t){
        s+=1440-p[i].e;
        e+=1440-p[i].e;
    }
    r.t=p[i].t;
    r.p=1440-p[i].e;
    ans+=(p[0].t^p[E.p-1].t);

    if(s<=720 && e>=720)
        return ans;
    sort(q,q+E.q,sort_cmp1);

    if(e<=720){
        t.p=t.p*t.t+r.p*r.t;
        t.t=t.t+r.t-(t.t^r.t);
        for(i=0;i<E.q;i++){
            if(e+t.p>=720)
                return ans+t.t;
            if(!q[i].t)
                continue;
            e+=q[i].p;
            ans+=2;
            if(e>=720)
                return ans;
        }
        if(e+t.p>=720)
            return ans+t.t;
    }
    else{
        t.p=t.p*(1-t.t)+r.p*(1-r.t);
        t.t=(1-t.t)+(1-r.t)-(t.t^r.t);
        for(i=0;i<E.q;i++){
            if(s-t.p<=720)
                return ans+t.t;
            if(q[i].t)
                continue;
            s-=q[i].p;
            ans+=2;
            if(s<=720)
                return ans;
        }
        if(s-t.p<=720)
            return ans+t.t;
    }

    return 0;
}
int main (void)
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    int T,i,j;

    scanf("%d",&T);

    for(i=1;i<=T;i++){
        scanf("%d %d",&E.b,&E.a);
        E.p=0;
        for(j=0;j<E.b;j++){
            scanf("%d %d",&b[j].s,&b[j].e);
            p[E.p].s=b[j].s;
            p[E.p].e=b[j].e;
            p[E.p++].t=1;
        }
        for(j=0;j<E.a;j++){
            scanf("%d %d",&a[j].s,&a[j].e);
            p[E.p].s=a[j].s;
            p[E.p].e=a[j].e;
            p[E.p++].t=0;
        }
        printf("Case #%d: %d\n",i,solve(i));
    }
    return 0;
}
