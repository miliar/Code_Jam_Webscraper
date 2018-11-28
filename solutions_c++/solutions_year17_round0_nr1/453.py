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
    int n;
    cin>>n;
    
    REP(t,n)
    {
        string s;
        int k;
        int cnt=0;
        bool flag=1;
        cin>>s>>k;
        REP(i,s.size())
        {
            if(s[i]=='-')
            {
                cnt++;
                FOR(j,i,i+k)
                {
                    if(j>=s.size())
                    {
                        flag=0;
                        break;
                    }
                    if(s[j]=='+')
                    s[j]='-';
                    else
                    s[j]='+';
                }
            }
        }

        cout<<"Case #"<<t+1<<": ";
        if(flag)
        {
            cout<<cnt<<endl;
        }
        else
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
}

