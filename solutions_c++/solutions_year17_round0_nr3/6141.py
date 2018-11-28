#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <queue>
using namespace std;

typedef long long ll;

priority_queue<int> p;

void solve()
{
    int t;
    cin>>t;
    for(int id=1;id<=t;id++)
    {
        while(!p.empty()) p.pop();
        ll a,b,tmp,t1,t2;
        cin>>a>>b;
        p.push(a);
        while(b--)
        {
            tmp=p.top();
            p.pop();
            if(tmp%2)
                t1=t2=(tmp-1)/2;
            else
            {
                t1=tmp/2-1;
                t2=tmp/2;
            }
            p.push(t1);
            p.push(t2);
        }
        printf("Case #%d: %lld %lld\n",id,t2,t1);
    }
}


int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    solve();
    return 0;
}
