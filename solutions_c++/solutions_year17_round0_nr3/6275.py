#include <bits/stdc++.h>
using namespace std;
multiset<int> s;
int main()
{
    int t;
    cin>>t;
    int tt=1;
  // freopen("in","r",stdin);
    freopen("out","w",stdout);
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        s.clear();
        s.insert(n);
        int l,r;
        for (int i=0;i<k;i++)
        {
            int x=*(--s.end());
            s.erase(--s.end());
            l=(x-1)/2;
            r=(x-1)/2+((x-1)%2);
            if (l!=0)
            s.insert(l);
            if (r!=0)
            s.insert(r);
        }
        cout<<"Case #"<<tt++<<": "<<r<<' '<<l<<endl;
    }
}
