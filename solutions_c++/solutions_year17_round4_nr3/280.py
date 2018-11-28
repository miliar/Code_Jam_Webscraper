#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          acos(-1)
#define sz(x)       (int)x.size()
string A[10];
bool fix[10][55];
int r,c;
bool solve()
{
    int i,j,k,l;
    bool flagh,flagv;
    vector<pii> v;
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            if(A[i][j]=='-'||A[i][j]=='|')
            {
                flagh=flagv=false;
                for(k=j+1;k<c&&A[i][k]!='#';k++)
                    if(A[i][k]=='-'||A[i][k]=='|')
                    {
                        flagh=true;
                        break;
                    }
                for(k=j-1;k>=0&&A[i][k]!='#';k--)
                    if(A[i][k]=='-'||A[i][k]=='|')
                    {
                        flagh=true;
                        break;
                    }
                for(k=i+1;k<r&&A[k][j]!='#';k++)
                    if(A[k][j]=='-'||A[k][j]=='|')
                    {
                        flagv=true;
                        break;
                    }
                for(k=i-1;k>=0&&A[k][j]!='#';k--)
                    if(A[k][j]=='-'||A[k][j]=='|')
                    {
                        flagv=true;
                        break;
                    }
                if(flagh&&flagv)
                    return false;
                if(flagh)
                {
                    A[i][j]='|';
                    fix[i][j]=true;
                }
                if(flagv)
                {
                    A[i][j]='-';
                    fix[i][j]=false;
                }
                if(!flagh&&!flagv)
                {
                    if(((i==0)||(A[i-1][j]=='#'))&&((i==r-1)||A[i+1][j]=='#'))
                    {
                        A[i][j]='-';
                        fix[i][j]=true;
                    }
                    if(((j==0)||A[i][j-1]=='#')&&((j==c-1)||A[i][j+1]=='#'))
                    {
                        A[i][j]='|';
                        fix[i][j]=true;
                    }
                }
                if(!fix[i][j])
                    v.pb({i,j});
            }
    for(i=0;i<(1<<sz(v));i++)
    {
        for(j=0;j<sz(v);j++)
            if(1&(i>>j))
                A[v[j].F][v[j].S]='|';
            else
                A[v[j].F][v[j].S]='-';
        for(j=0;j<r;j++)
            for(k=0;k<c;k++)
                if(A[j][k]=='.')
                {
                    flagh=flagv=false;
                    for(l=k+1;l<c&&A[j][l]!='#';l++)
                        if(A[j][l]=='-')
                    {
                        flagh=true;
                        break;
                    }
                    for(l=k-1;l>=0&&A[j][l]!='#';l--)
                        if(A[j][l]=='-')
                    {
                        flagh=true;
                        break;
                    }
                    for(l=j+1;l<r&&A[l][k]!='#';l++)
                        if(A[l][k]=='|')
                    {
                        flagv=true;
                        break;
                    }
                    for(l=j-1;l>=0&&A[l][k]!='#';l--)
                        if(A[l][k]=='|')
                    {
                        flagv=true;
                        break;
                    }
                    if(!flagh&&!flagv)
                    {
                        j=r+1;
                        k=c+1;
                        break;
                    }
                }
        if(j==r&&k==c)
            return true;
    }
    return false;
}
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,i,j;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>r>>c;
        memset(fix,false,sizeof fix);
        for(i=0;i<r;i++)
            cin>>A[i];
        cout<<"Case #"<<t<<": ";
        if(solve())
        {
            cout<<"POSSIBLE"<<endl;
            for(i=0;i<r;i++)
                cout<<A[i]<<endl;
        }
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
