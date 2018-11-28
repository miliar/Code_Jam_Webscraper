#include<bits/stdc++.h>

using namespace std;

#define li long int
#define ii pair<li,li>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define vi vector<li>
#define vii vector<ii>
#define INF 99999
#define MAXN 100005
#define sz size()
#define ins insert

#include<bits/stdc++.h>
using namespace std;

typedef long long       LL;

#define REP(i,n) for(__typeof(n) i = 0; i < n; i++)
#define REP1(i,n) for(__typeof(n) i = 1; i <= n; i++)


int main()
{
    freopen("E:\\input.txt","r",stdin);
    freopen("E:\\output.txt","w",stdout);

   li t; cin >> t;
    REP1(test, t){
        string s[26];
        int k,r,c;
        cin>>r>>c;
       REP(i, r) cin>>s[i];
       REP(i, r)
            REP(j, c)
                if(s[i][j]!='?')
                {
                    k=j;
                    while(k+1<c && s[i][k+1]=='?') { s[i][k+1]=s[i][k]; k++; }

                   k=j;
                    while(k-1>=0 && s[i][k-1]=='?') { s[i][k-1]=s[i][k]; k--; }
                }
       REP(i, r)
            if(s[i][0]=='?')
            {
                if(i-1>=0)
                    REP(j, c) s[i][j]=s[i-1][j];
                else if (i+1<r)
                    REP(j, c) s[i][j]=s[i+1][j];
            }

       for(int i=r-1;i>=0;i--)
        {
            if(s[i][0]=='?')
            {
                if(i-1>=0)
                {
                    REP(j, c) s[i][j]=s[i-1][j];
                }
                if (i+1<r)
                {
                    REP(j, c) s[i][j]=s[i+1][j];
                }
            }
        }
       cout<<"Case #"<<test<<":"<<endl;

       REP(i, r)
        {
            REP(j, c) cout<<s[i][j];
            cout<<endl;
        }
    }
    return 0;
}
