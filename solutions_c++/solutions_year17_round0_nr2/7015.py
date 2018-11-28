#include <bits/stdc++.h>
#define int long long int
using namespace std;
main()
{
    freopen("inputt.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,c=1;
    string n;
    //cout<<"lol";
    cin>>t;
    //t=1;
    while(t--)
    {
        cin>>n;
        //n=10;
        //cout<<"lol";
        cout<<"Case #"<<c<<": ";
        c++;
        int l=n.length(),pos=-1;
        for(int i=0; i<l-1; i++)
        {
            if(n[i]>n[i+1])
            {
                pos=i;
                break;
            }
        }
        if(pos==-1)
            cout<<n<<endl;
        else
        {
            int flag=0,pos2;
            for(int i=pos; i>=0; i--)
            {
                if(n[i]!=n[pos])
                {
                    flag=1;
                    pos2=i;
                    break;
                }
            }
            if(flag)
            {
                n[pos2+1]--;
                for(int i=pos2+2; i<l; i++)
                {
                    n[i]='9';
                }
            }
            else
            {
                n[0]--;
                for(int i=1; i<l; i++)
                {
                    n[i]='9';
                }
                if(n[0]=='0')
                {
                    n=n.substr(1,l-1);
                }
            }
            cout<<n<<endl;
        }
    }
    return 0;
}
