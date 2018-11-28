#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output_large.txt","w",stdout);
    int q,k,cou,flag;
    string s;
    cin>>q;
    int z=1;
    while(z!=q+1)
    {
        cin>>s>>k;
        cou = 0;flag = 1;
        for(int i=s.length()-1;i>=k-1;i--)
        {
            if(s[i]=='-')
            {
                cou++;
                for(int j=i;j>i-k;j--)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                flag = 0;
                break;
            }
        }
        //cout<<s<<endl;
        if(flag ==1)
            cout<<"Case #"<<z<<": "<<cou<<endl;
        else
            cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
        z++;
    }
    return 0;
}

