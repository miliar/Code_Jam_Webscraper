#include <iostream>
using namespace std;
typedef long long ll;
int main()
{
    ios::sync_with_stdio(false);
    int T,cas=0;
    cin >> T;
    while(T--)
    {
        cout << "Case #" << ++cas << ": ";
        ll N,K;
        cin >> N >> K;
        int flag=1;
        ll w=1;
        ll top=0;
        ll l=N,r=N;
        ll cntl=0,cntr=1;
        if((N>>1)&1) flag=1;
        else if(((N-1)>>1)&1) flag=2;
        else flag=3;
        while(top+w<K)
        {
            top+=w;
            w<<=1;
            ll tl=0,tr=0;
            if(r&1)
                tr+=cntr<<1;
            else tr+=cntr,tl+=cntr;
            if(l&1)
                tl+=cntl<<1;
            else tl+=cntl,tr+=cntl;
            cntl=tl,cntr=tr;
            l=(l-1)>>1,r=r>>1;
        }
        if(top+cntr>=K)
            l=(r-1)>>1,r=r>>1;
        else
            r=l>>1,l=(l-1)>>1;

        cout << max(0ll,r) << " " << max(0ll,l) << endl;
    }
    return 0;
}
