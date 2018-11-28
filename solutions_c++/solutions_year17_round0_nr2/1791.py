#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define bp __builtin_popcount

#define mt(a,b,c) mp(a,mp(b,c))
#define min3(a,b,c) min(a,min(b,c))

const ll mo=1e9+7;
const ll INF=1e17;
const ld pi=acos(-1);
const int mxn=2e5+5;
const int cons=1;

using namespace std;

string rem0(string s)
{
    int i;
    for(i=0;i<(int)s.length();i++)
    {
        if(s[i]!='0')
        {
            return s.substr(i,s.length()-i);
        }
    }
}

bool chk(string s)
{
    int i;
    for(i=0;i<(int)s.length()-1;i++)
    {
        if(s[i]>s[i+1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T,t,i,j;
    string s,p;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>s;
        for(i=s.length();i>=0;i--)
        {
            p=s;
            if(i!=(int)s.length())
            {
                p[i]=(char)(s[i]-1);
            }
            for(j=i+1;j<(int)s.length();j++)
            {
                p[j]='9';
            }
            if(chk(p))
            {
                break;
            }
        }
        cout<<rem0(p)<<"\n";
    }
    return 0;
}
