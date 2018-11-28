#include<bits/stdc++.h>
using namespace std;

string s;
void flips(int p,int k)
{
    for(int j=0;j<k;j++)
    {
        if(s[p]=='-')
        s[p]='+';
        else
        s[p]='-';
        p++;
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,flip=0,k,l,j,i,f=0,c=1;
    cin>>t;
    while(t--)
    {
        flip = 0;f=0;
        cin>>s;
        cin>>k;
        l=s.length();
        for(i=0;i<l;i++)
        {
            if(s[i]=='-' && (i+k)<=l)
            {
                flips(i,k);
                flip++;
            }
        }

        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                f=1;
            }

        }

        if(f==1)
        cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<c<<": "<<flip<<endl;
        c++;
        }
}

