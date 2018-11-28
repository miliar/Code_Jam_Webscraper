#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll arr[100100],t,n,r,o,y,g,b,v,red,yellow,blue,maxi;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cout<<"Case #"<<j<<": ";
        cin>>n>>r>>o>>y>>g>>b>>v;
        maxi=max(r,max(y,b));
        if(maxi==r)
        {
            if(maxi<=(y+b))
            {
                while(maxi!=(y+b))
                {
                    if(y<=b)
                        cout<<"RBY";
                    else
                        cout<<"RYB";
                    maxi--,y--,b--;
                }
                while(y!=0)
                    cout<<"RY",y--;
                while(b!=0)
                    cout<<"RB",b--;
            }
            else
                cout<<"IMPOSSIBLE";
        }
        else if(maxi==y)
        {
            if(maxi<=(r+b))
            {
                while(maxi!=(r+b))
                {
                    if(r<=b)
                        cout<<"YBR";
                    else
                        cout<<"YRB";
                    maxi--,r--,b--;
                }
                while(r!=0)
                    cout<<"YR",r--;
                while(b!=0)
                    cout<<"YB",b--;
            }
            else
                cout<<"IMPOSSIBLE";
        }
        else if(maxi==b)
        {
            if(maxi<=(r+y))
            {
                while(maxi!=(r+y))
                {
                    if(r<=y)
                        cout<<"BYR";
                    else
                        cout<<"BRY";
                    maxi--,r--,y--;
                }
                while(r!=0)
                    cout<<"BR",r--;
                while(y!=0)
                    cout<<"BY",y--;
            }
            else
                cout<<"IMPOSSIBLE";
        }
        cout<<endl;
    }
return 0;
}
