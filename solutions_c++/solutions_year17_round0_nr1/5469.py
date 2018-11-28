#include <bits/stdc++.h>
#define ll long long int
#define fs first
#define sc second
#define pb push_back
#define ppb pop_back
#define pii pair<int,int>
#define pil pair<int,ll>
#define vll vector<ll>
#define vi vector<int>
#define d0(x) cout<<x<<" "
#define d1(x) cout<<x<<"\n"
#define d2(x,y) cout<<x<<" "<<y<<"\n"
#define d3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n"
const ll mod=1e9+7;int s[2000];
using namespace std;
int main()
{
    ios_base::sync_with_stdio ( false );
    ofstream outp("output.txt");
    ifstream inp("input.txt");
    int t;inp>>t;
    for(int test=1;test<=t;test++)
    {
        string s1;inp>>s1;int ln=s1.size();
        for(int i=0;i<ln;i++)
        {
            if(s1.at(i)=='+')
            {
                s[i]=1;
            }
            else
            {
                s[i]=0;
            }
        }
        int k;inp>>k;int cnt=0;
        for(int i=ln-1;i>=k-1;i--)
        {
            if(s[i]==0)
            {
                cnt++;
                for(int j=i;j>i-k;j--)
                {
                    s[j]=(s[j]+1)%2;
                }
            }
        }
        bool ans=true;
        for(int i=0;i<ln;i++)
        {
            if(s[i]==0)
            {
                ans=false;
            }
        }
        outp<<"Case #"<<test<<": ";
        if(ans)
        {
             outp<<cnt<<"\n";
        }
        else
        {
            outp<<"IMPOSSIBLE\n";
        }
    }
}
