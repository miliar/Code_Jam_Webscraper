#include <bits/stdc++.h>
using namespace std;
typedef double ld;
#define y1 cgbngfgn
#define pb push_back
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define fir first
#define m_p make_pair
#define sec second
#define files(name) freopen(name".sol","r",stdin); freopen (name".dat","w",stdout);
int a[20000];
signed main()
{
    files("graph");
    int t;
    cin>>t;
    for (int l=1;l<=t;l++)
    {
        string st;
        cin>>st;
        int k;
        cin>>k;
        for (int i=0;i<st.size();i++)
        {
            a[i+1]=(st[i]=='+');
        }
        bool ch=1;
        int n=st.size();
        int ans=0;
        for (int i=1;i<=n;i++)
            if (!a[i])
        {
            if (i+k-1>n && ch)
            {
                cout<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<'\n';
                ch=0;
            }
            if (!ch) break;
            ans++;
            for (int j=i;j<=i+k-1;j++)
                a[j]=!a[j];
        }
        if (ch)
        cout<<"Case #"<<l<<": "<<ans<<'\n';
    }


}
