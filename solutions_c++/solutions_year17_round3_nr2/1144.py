#include<stdio.h>
#include<math.h>
#include<algorithm>
#define N 105
using namespace std;
struct emp{
    int a,b,p,q,s,e,t;
};
emp n,a[N],b[N],p[2*N],q[2*N];
int ans;
bool sort_cmp(emp x,emp y){
    return x.s<y.s;
}
bool sort_cmp_1(emp x,emp y){
    return x.p>y.p;
}
int solve(int tt){
    int i,x,y,s,e;
    emp t,r;
    t.t=t.p=r.t=r.p=0;
    sort(a,a+n.a,sort_cmp);
    sort(b,b+n.b,sort_cmp);
    sort(p,p+n.p,sort_cmp);
    s=e=x=y=0;
    n.q=0;
    ans=0;
    if(!p[0].t) s=e=p[0].s;
    t.t=p[0].t;
    t.p=p[0].s;
    for(i=0;i<n.p-1;i++){
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
            q[n.q].t=p[i].t;
            q[n.q++].p=(p[i+1].s-p[i].e);
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
    ans+=(p[0].t^p[n.p-1].t);
    if(s<=720 && e>=720)    return ans;
    sort(q,q+n.q,sort_cmp_1);
    if(e<=720){
        t.p=t.p*t.t+r.p*r.t;
        t.t=t.t+r.t-(t.t^r.t);
        for(i=0;i<n.q;i++){
            if(e+t.p>=720)  return ans+t.t;
            if(!q[i].t)  continue;
            e+=q[i].p;
            ans+=2;
            if(e>=720)  return ans;
        }
        if(e+t.p>=720)  return ans+t.t;
    }else{
        t.p=t.p*(1-t.t)+r.p*(1-r.t);
        t.t=(1-t.t)+(1-r.t)-(t.t^r.t);
        for(i=0;i<n.q;i++){
            if(s-t.p<=720)  return ans+t.t;
            if(q[i].t) continue;
            s-=q[i].p;
            ans+=2;
            if(s<=720)  return ans;
        }
        if(s-t.p<=720)  return ans+t.t;
    }
    return 0;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,tt,i;
    scanf("%d",&test);

    for(tt=1;tt<=test;tt++){
        scanf("%d %d",&n.b,&n.a);
        n.p=0;
        for(i=0;i<n.b;i++){
            scanf("%d %d",&b[i].s,&b[i].e);
            p[n.p].s=b[i].s;
            p[n.p].e=b[i].e;
            p[n.p++].t=1;
        }
        for(i=0;i<n.a;i++){
            scanf("%d %d",&a[i].s,&a[i].e);
            p[n.p].s=a[i].s;
            p[n.p].e=a[i].e;
            p[n.p++].t=0;
        }
        printf("Case #%d: %d\n",tt,solve(tt));
    }
    return 0;
}
