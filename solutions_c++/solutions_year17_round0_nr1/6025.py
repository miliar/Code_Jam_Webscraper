///apac question 2 round 1 , 2017
#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
#define pi acos(-1)
#include<string.h>
#define rep(i,n) for(i=0;i<n;i++)
#define pb push_back
using  namespace std;
typedef long long int lli;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<int> vi;
typedef  vector<vi> vvi;
typedef vector<lli> vlli;
typedef vector<double> vd;
typedef map<int,int> mpii;
typedef map<string,int> mpsi;
typedef tuple<int,int,int> tiii ;
typedef vector<tiii> vtiii ;
#define mp make_pair
#define modu 1000000007
int main()
{
    freopen("inputaa.in","r",stdin);
    freopen("outputa.out","w",stdout);
    lli test,t,k,c,n,i,j;
    string s;
    cin>>test;
    for(t=0;t<test;t++)
    {
        cin>>s>>k;;
        c=0;
        n=s.size();
        for(i=0;i<n-k+1;i++)
            if(s[i]=='-')
                {
                    c++;
                    for(j=i;j<=i+k-1;j++)
                        if(s[j]=='-')s[j]='+';
                        else s[j]='-';
                }

        for(i=n-k+1;i<n;i++)
            if(s[i]=='-'){
                    cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
                    goto no;
            }

        cout<<"Case #"<<t+1<<": "<<c<<endl;
        no:;
    }
}
