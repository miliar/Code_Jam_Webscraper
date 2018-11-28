#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
using namespace std;
char a[50][50];
vector<int> v[50];
int main()
{
    //freopen("data2.in","r",stdin);
    //freopen("out2.txt","w",stdout);
    int r,c,i,j,k,l,l1=0,t;
    cin>>t;
    while(t--){
    cin>>r>>c;
    for(i=0;i<r;i++)
    {
        v[i].clear();
        for(j=0;j<c;j++)
        {
            cin>>a[i][j];
            if(a[i][j]!='?')
                v[i].pb(j);
        }
        //v[i].pb(c);
    }
    /*tr(v[2],it)
    {
        cout<<*it;
    }*/
    int l2;
    for(k=0;k<r;k++)
    {
        for(l=0;l<c;l++)
        {
            for(i=0;i<r;i++)
            {
                if(v[i].size())
                {
                    l2=0;
                    char ch;
                    tr(v[i],it)
                    {
                        ch=a[i][*it];
                        for(;l2<=(*it);l2++)
                        {
                            a[i][l2]=ch;
                        }
                    }
                    for(;l2<c;l2++)
                    {
                        a[i][l2]=ch;
                    }
                    continue;
                }
                else if(i>0&&v[i-1].size())
                {
                    for(l2=0;l2<c;l2++)
                    {
                        a[i][l2]=a[i-1][l2];
                       if(a[i][l2]!='?')
                        v[i].pb(l2);
                    }
                }
                else if(i<r&&v[i+1].size())
                {
                    for(l2=0;l2<c;l2++)
                    {
                        a[i][l2]=a[i+1][l2];
                        if(a[i][l2]!='?')
                            v[i].pb(l2);
                    }
                }
            }
        }
    }
    l1++;
    cout<<"Case #"<<l1<<":\n";
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            cout<<a[i][j];
        }
        cout<<"\n";
    }
    }
    return 0;
}
