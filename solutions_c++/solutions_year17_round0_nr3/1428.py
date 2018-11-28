#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    long long K;
    long long b,s,nb,ns;
    long long tb,ts,nnb,nns;
    long long accum;
    scanf("%d",&T);
    for(int kase=1;kase<=T;++kase)
    {
        cin>>b>>K;
        nb=1;s=0;ns=0;accum=1;
        while(accum<K)
        {
            ts=0;nnb=nns=0;
            if(b&1)
            {
                tb=(b-1)/2;
                nnb+=2*nb;
            }
            else
            {
                tb=b/2;
                ts=b/2-1;
                nnb+=nb;
                nns+=nb;
            }
            if(s)
            {
                if(s&1)
                {
                    ts=(s-1)/2;
                    nns+=2*ns;
                }
                else
                {
                    ts=s/2-1;
                    nnb+=ns;
                    nns+=ns;
                }
            }
            nb=nnb;ns=nns;
            b=tb;s=ts;
            if(b) accum+=nb;
            if(s) accum+=ns;
            //cout<<b<<" "<<nb<<" | "<<s<<" "<<ns<<endl;
            //cout<<accum<<endl;
        }
        if(b) accum-=nb;
        if(s) accum-=ns;
        K-=accum;
        long long chk;
        if(K<=nb) chk=b;
        else chk=s;
        printf("Case #%d: ",kase);
        if(chk&1)
            cout<<(chk-1)/2<<" "<<(chk-1)/2<<endl;
        else
            cout<<chk/2<<" "<<chk/2-1<<endl;
    }
    return 0;
}
