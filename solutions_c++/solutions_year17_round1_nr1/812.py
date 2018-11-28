#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int
#define mod 1000000007


long long int powe(long long int x, long long int y, long long int m)
{
    if (y == 0)
        return 1;
    long long int p = powe(x, y/2, m) % m;
    p = (p * p) % m;
    return (y%2 == 0)? p : (x * p) % m;
}

int main()
{
    int t,ti;
    cin>>t;
    rep(ti,1,t)
    {
        int i,j,r,c,ii,jj,flag=0,flag2;
        cin>>r>>c;
        string s[28];
        char ans[28][28],lastch='?';
        rep(i,0,r-1)
            cin>>s[i];
        rep(i,0,r-1)
        {
            char ch='?';
                flag2=0;
            rep(j,0,c-1)
            {
                if(s[i][j]!='?')
                    ch=s[i][j];

                if(ch!='?'&&flag2==0)
                {
                    flag2=1;
                    rep(ii,0,j)
                        ans[i][ii]=ch;
                }
                else if(ch!='?')
                    ans[i][j]=ch;
            }
                if(flag==0&&ch!='?')
                {
                    flag=1;
                    rep(ii,0,i-1)
                    {
                        rep(jj,0,c-1)
                            ans[ii][jj]=ans[i][jj];
                    }
                }
            if(ch=='?'&&flag==1)
            {
                rep(j,0,c-1)
                ans[i][j]=ans[i-1][j];
            }
        }
        printf("Case #%d:\n",ti);
        rep(i,0,r-1)
        {
            rep(j,0,c-1)
                cout<<ans[i][j];
            cout<<"\n";
        }
    }
        return 0;
}
