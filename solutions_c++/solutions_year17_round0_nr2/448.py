#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef long double LD;
typedef pair<LD, LD> PLDLD;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))
#define ALL(a) a.begin(),a.end()

const double eps=1e-5;
const int INF=1e9;

int main()
{
    int t;
    cin>>t;
    
    REP(tt,t)
    {
        string s;
        cin>>s;

        bool f=1;
        while(f)
        {
            f=0;
            REP(i,s.size()-1)
            {
                if(s[i]>s[i+1])
                {
                    f=1;
                    s[i]--;
                    FOR(j,i+1,s.size())
                    {
                        s[j]='9';
                    }
                    break;
                }
            }
        }
        if(s[0]=='0')
            s=s.substr(1);
        
        cout<<"Case #"<<tt+1<<": "<<s<<endl;

    }
}

