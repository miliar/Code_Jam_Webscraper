#include<bits/stdc++.h>
#include<conio.h>
#define ll long long
using namespace std;
main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T=1;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        int k,l=s.size();
        cin>>k;
        int i=0,c=0;
        bool p=0;
        while(1)
        {
            if(s[i]=='-')
            {
                if(i+k<=l)
                {
                    c++;
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                }
                else
                {
                    p=1;
                    break;
                }
            }
            i++;
            if(i==l)
                break;
        }
        if(p==0)
            cout<<"Case #"<<T<<": "<<c<<'\n';
        else
            cout<<"Case #"<<T<<": "<<"Impossible\n";
        T++;
    }
}
