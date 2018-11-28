#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    freopen ("inp","r",stdin);
    freopen ("outp1","w",stdout);
    int t;
    cin>>t;
    for (int pp=1;pp<=t;pp++)
    {
        int n;
        string s;
        cin>>s;
        cin>>n;
        int k=0;
        for (int i=0;i<=(int)s.size()-n;i++)
        {
            if (s[i]=='-')
            {
                k++;
                for (int j=i;j<i+n;j++)
                {
                    if (s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        bool f=1;
        for (int i=(int)s.size()-n;i<s.size();i++)
        {
            if (s[i]=='-')
            {
                f=0;
            }
        }
        if (f==0)
            cout<<"Case #"<<pp<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<pp<<": "<<k<<endl;
    }

}
