
/*****************************************
Author: lizi
Email: lzy960601@outlook.com
****************************************/
  
#include<bits/stdc++.h>
  
using namespace std;
  
const double eps=1e-10;
const double pi=3.1415926535897932384626433832795;
const double eln=2.718281828459045235360287471352;
  
#define LL long long
#define IN freopen("Cl.in", "r", stdin)
#define OUT freopen("Cl.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%lld: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))

priority_queue<LL> q;
LL T,n,m;
map<LL,LL> pp;

int main()
{
    IN;OUT;
    cin>>T;
    for(LL t=1;t<=T;t++)
    {
        cin>>n>>m;pp.clear();
        while(!q.empty())q.pop();
        q.push(n);pp[n]=1;
        prr(t);
        while(1)
        {
            LL x=q.top();q.pop();
            if(pp[x]==0)continue;
            LL a=x/2;
            LL b=(x-1)/2;
            if(m<=pp[x]){printf("%lld %lld\n",a,b);break;}
            if(pp[a]==0)q.push(a);pp[a]+=pp[x];
            if(pp[b]==0)q.push(b);pp[b]+=pp[x];
            m-=pp[x];pp[x]=0;
        }
    }
    return 0;
}
