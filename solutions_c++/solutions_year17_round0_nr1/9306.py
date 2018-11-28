#include<bits/stdc++.h>
#define f first

using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    freopen("in.cpp","r",stdin);
    freopen("out2.txt","w",stdout);
    long long t,n,k,q,l,r,i,j,x,y,z,x1,x2,y1,y2;
    vector<long long>a,b;
    cin>>t;l=1;
    while(t--)
    {
        string s;
        cin>>s>>k;
        x=s.size();z=0;y=0;
        for(i=0;i<=x-k;i++)
        {
            if(s[i]=='-')
            {
               for(j=i;j<i+k;j++)
               {
                   if(s[j]=='-')
                    s[j]='+';
                   else
                    s[j]='-';
               }
               z++;
            }
        }
        for(i=x-k+1;i<x;i++)
        {
            if(s[i]=='-')
            {
                y=1;break;
            }
        }
        cout<<"Case #"<<l<<": ";
        if(y==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<z<<endl;
        l++;

    }
    return 0;
}


