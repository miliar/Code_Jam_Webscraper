#include<bits/stdc++.h>
using namespace std;
int main()
{

    int t,l,i,j;
    char s[20];
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int min1=100;
        cin>>s;
        l=strlen(s);

        for(i=l-1;i>0;i--)
        {

                if(s[i]<s[i-1])
                {
                    s[i-1]-=1;
                    for(int u=i;u<l;u++)
                    {
                        s[u]='9';
                    }
                }

        }
        if(s[0]=='0')
        {
            cout<<"Case #"<<k<<": "<<s+1<<endl;
        }
        else
            cout<<"Case #"<<k<<": "<<s<<endl;
    }
    return 0;
}
