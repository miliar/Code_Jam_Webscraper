#include <bits/stdc++.h>
using namespace std;
multiset <int> otr;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    otr.clear();
    for (int i=1;i<=t;i++)
    {
        int n,k,ans1,ans2;
        cin>>n>>k;
        otr.clear();
        otr.insert(n);
        for (int j=1;j<=k;j++)
        {
            int to=*(otr.rbegin());
            multiset <int>::iterator it=otr.end();
            it--;
            otr.erase(it);
            if (to%2==1)
            {
                ans1=(to-1)/2;
                ans2=(to-1)/2;
            }
            else
            {
                ans1=to/2-1;
                ans2=to/2;
            }
            if (ans1!=0) otr.insert(ans1);
            if (ans2!=0) otr.insert(ans2);
        }
        cout<<"Case #"<<i<<": "<<ans2<<' '<<ans1<<'\n';
    }
    return 0;
}
