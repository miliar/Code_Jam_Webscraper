#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        string x;
        cin>>x;
        int uk=0,uks=0;
        bool fl=true;
        while (uk<(int)x.length() && fl)
        {
            uk=uks;
            while (uks<(int)x.length() && x[uks]==x[uk]) uks++;
            if (uks<(int)x.length())
                if ((int)x[uks]<(int)x[uk]) fl=false;
        }
        if (fl)
            cout<<"Case #"<<i<<": "<<x<<'\n';
        else
        {
            cout<<"Case #"<<i<<": ";
            for (int j=0;j<uk;j++)
                cout<<x[j];
            if (x[uk]!='1') cout<<(char)((int)x[uk]-1);
            for (int j=uk+1;j<(int)x.length();j++)
                cout<<'9';
            cout<<'\n';
        }
    }
    return 0;
}

