#include <cstring>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#define LL long long
using namespace std;
LL n,k,tmp;

LL b[2],cnt[2];
LL p,q,cp,cq;
int now;
int main()
{
    #ifdef VGel
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    #endif // VGel
    int T_T;
    scanf("%d",&T_T);
    for (int T=1;T<=T_T;T++)
    {
        scanf("%lld%lld",&n,&k);
        int top=1;
        while (n>=((LL)1<<top)) top++;
        int len=0;
        tmp=k;
        while (tmp) {++len;tmp>>=1;}
        if (len>=top) {printf("Case #%d: 0 0\n",T);continue;}
        b[0]=n;cnt[0]=1;now=1;

//        cout<<now<<"--"<<b[0]<<" "<<cnt[0]<<"     "<<b[1]<<" "<<cnt[1]<<endl;
        for (int i=len-1;i>=1;i--)
        {
            p=b[0];cp=cnt[0];
            q=b[1];cq=cnt[1];
            int pre=now;

            if (p%2) {now=1;b[0]=(p-1)>>1;cnt[0]=cp<<1;b[1]=-1;cnt[1]=0;}
            else {now=2;b[0]=p>>1;cnt[0]=cp;b[1]=b[0]-1;cnt[1]=cp;}

            if (pre==2&&q!=0)
            {
                if (q%2) {cnt[now-1]+=cq<<1;}
                else {now=2;cnt[0]+=cq;b[1]=b[0]-1;cnt[1]=cq;}
            }
//            cout<<now<<"--"<<b[0]<<" "<<cnt[0]<<"     "<<b[1]<<" "<<cnt[1]<<endl;
        }
        k-=((LL)1<<len-1)-1;
//        cout<<k<<endl;

        tmp=(cnt[0]<k)?b[1]:b[0];
//        cout<<tmp<<endl;
        if (tmp%2) {p=(tmp-1)>>1;q=(tmp-1)>>1;}
        else {p=tmp>>1;q=(tmp-1)>>1;}
        printf("Case #%d: %lld %lld\n",T,p,q);
    }
    return 0;
}

