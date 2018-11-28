
#include<bits/stdc++.h>
using namespace std;
int a[2000];
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
    int tt=1;
    while(t--)
    {
        string s;
        cin>>s;
        int k;
        cin>>k;
        memset(a,0,sizeof(a));
        int now=0;
        int n=s.size();
        int num=0;
        bool no=0;
        for (int i=0;i<n;i++)
        {
            now+=a[i];
            if (now%2)
            {
                if (s[i]=='+')s[i]='-';
                else s[i]='+';
            }
            if (s[i]=='-')
            {
                if (i+k>n)
                    no=1;
                else{
                s[i]='+';
                now++,a[i+k]--;
                num++;
                }
            }
        }
        cout<<"Case #"<<tt++<<": ";
        if (no)cout<<"IMPOSSIBLE"<<endl;
        else cout<<num<<endl;
    }

}
