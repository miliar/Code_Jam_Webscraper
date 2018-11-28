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
        LL n,k;
        cin>>n>>k;
        LL c=2;
        LL sm=n-1,la=n;
        LL smn=0,lan=1;
        LL psmn, plan;
        while(c-1<k)
        {
            psmn=smn;
            plan=lan;
            smn=0;
            lan=0;
            if(la%2==0)
            {
                la/=2;
                lan+=plan;
                smn+=plan;

                sm=(sm-1)/2;
                smn+=psmn*2;
            }
            else
            {
                la=(la-1)/2;
                lan+=plan*2;

                sm=(sm-1)/2;
                lan+=psmn;
                smn+=psmn;
            }

            c<<=1;
        }
        c>>=1;
        c--;
        LL ansl,anss;
        if(k-c<=lan)
        {
            ansl=la/2;
            anss=(la-1)/2;
        }
        else
        {
            ansl=sm/2;
            anss=(sm-1)/2;
        }
        cout<<"Case #"<<tt+1<<": "<<ansl<<" "<<anss<<endl;
    }
}

