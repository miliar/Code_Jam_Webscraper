#include <bits/stdc++.h>
using namespace std;
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef pair<int,int> PII;
const double eps=1e-8;
const double pi=acos(-1.0);
const int K=1e6+7;
const int mod=1e9+7;
int main(void)
{
    int t,cnt=1;
    //freopen("A-large.in","r",stdin);
    freopen("c.out","w",stdout);
    cin>>t;
    while(t--)
    {
        LL n,k,ansl,ansr,a,b=0,sa=1,sb=0,sum=0,ls=1,ta,tb,sta,stb,pa,pb,spa,spb;
        cin>>n>>k;
        a=n;
        for(int i=1;sum+ls<k;i++)
        {
            sum+=ls,ls*=2;
            ta=tb=sta=stb=pa=pb=spa=spb=0;
            if(a&1)
                tb=a/2,stb=sa*2;
            else
                ta=a/2-1,tb=a/2,sta=stb=sa;
            if(b!=0)
            {
                if(b&1)
                    pa=b/2,spa=sb*2;
                else
                    pa=b/2-1,pb=b/2,spa=spb=sb;
            }
            a=tb,sa=stb,sb=sta;
            if(b)
            {
                if(a==pa)   sa+=spa,sb+=spb;
                else if(a==pb)   sa+=spb,sb+=spa;
                else sb+=spa;
                if(a==pa&&pb)b=pb;
                else if(a==pb&&pa)b=pa;
                else b=ta;
            }
            else b=ta;
            if(a<b)
                swap(a,b),swap(sa,sb);
            //printf("     debug::==> %I64d:%I64d==%I64d:%I64d %I64d\n",a,sa,b,sb,sum);
        }
        k-=sum;
        //printf("     debug::==> %I64d:%I64d==%I64d:%I64d k:%d\n",a,sa,b,sb,k);
        if(k>sa)    a=b;
        if(a&1) ansl=ansr=a/2;
        else    ansl=a/2-1,ansr=a/2;
        ansl=max(ansl,0LL),ansr=max(ansr,0LL);
        if(ansl<ansr)swap(ansl,ansr);
        printf("Case #%d: %I64d %I64d\n",cnt++,ansl,ansr);
    }
    return 0;
}

