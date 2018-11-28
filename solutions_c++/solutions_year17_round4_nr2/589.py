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
int N,M;
bool bpm(bool bpGraph[][1005], int u, bool seen[], int matchR[])
{
    for (int v = 0; v < N; v++)
    {
        if (bpGraph[u][v] && !seen[v])
        {
            seen[v] = true;
            if (matchR[v] < 0 || bpm(bpGraph, matchR[v], seen, matchR))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
int matchR[1005];
int maxBPM(bool bpGraph[][1005])
{
    memset(matchR, -1, sizeof(matchR));
    int result = 0;
    for (int u = 0; u < M; u++)
    {
        bool seen[N];
        memset(seen, 0, sizeof(seen));
        if (bpm(bpGraph, u, seen, matchR))
            result++;
    }
    return result;
}
bool A[1005][1005];
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,i,j,n,c,m,p,b,r,pr;
    vi c1,c2;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n>>c>>m;
        c1.clear();
        c2.clear();
        while(m--)
        {
            cin>>p>>b;
            if(b==1)
                c1.pb(p);
            if(b==2)
                c2.pb(p);
        }
        memset(A,false,sizeof A);
        M=sz(c1);
        N=sz(c2);
        for(i=0;i<sz(c1);i++)
            for(j=0;j<sz(c2);j++)
                if(c1[i]!=c2[j])
                    A[i][j]=true;
        r=pr=0;
        r=maxBPM(A);
        if(r==sz(c1))
            r=sz(c2);
        else if(r==sz(c2))
            r=sz(c1);
        else
        {
            for(i=0;i<N;i++)
                if(matchR[i]<0)
                    break;
            if(c2[i]==1)
                r+=sz(c1)-r+sz(c2)-r;
            else
            {
                int maxi=max(sz(c1)-r,sz(c2)-r);
                int mini=min(sz(c1)-r,sz(c2)-r);
                r+=maxi;
                pr+=mini;
            }
        }
        cout<<"Case #"<<t<<": "<<r<<" "<<pr<<endl;
    }
    return 0;
}
