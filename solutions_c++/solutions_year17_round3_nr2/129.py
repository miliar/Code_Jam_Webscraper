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
const LL INF=1e15;
const LD pi=3.141592653589793238462643383279502884;


int main()
{
    int tt;
    cin>>tt;
    REP(l,tt)
    {
        using  TIII=tuple<int,int,int>;
        int ac,aj;
        int ct=720,jt=720;
        cin>>ac>>aj;
        vector<TIII> t;
        REP(i,ac)
        {
            int c,d;
            cin>>c>>d;
            ct-=d-c;
            t.push_back(TIII(c,d,0));
        }
        REP(i,aj)
        {
            int c,d;
            cin>>c>>d;
            jt-=d-c;
            t.push_back(TIII(c,d,1));
        }
        sort(ALL(t));
        int ans=0;
        int cj=-1;
        vector<int> crm,jrm;
        auto tmp=t[0];
        int p,q,r;
        tie(p,q,r)=tmp;
        cj=r;
        FOR(i,1,t.size()+1)
        {
            if((i)%t.size()==0)
            {
                tmp=t[(i)%t.size()];
                tie(p,q,r)=tmp;
                p+=1440;
                q+=1440;
            }
            else
            {
                tmp=t[(i)%t.size()];
                tie(p,q,r)=tmp;
            }

            if(cj==0)
            {
                if(r==0)
                {
                    crm.push_back(p-get<1>(t[i-1]));
                    ans+=2;
                }
                else
                {
                    ans++;
                }
            }
            else
            {
                if(r==1)
                {
                    jrm.push_back(p-get<1>(t[i-1]));
                    ans+=2;
                }
                else
                {
                    ans++;
                }
            }
            cj=r;
        }

        sort(ALL(crm));
        sort(ALL(jrm));
        REP(i,crm.size())
        {
            if(crm[i]<=ct)
            {
                ans-=2;
                ct-=crm[i];
            }
            else break;
        }
        REP(i,jrm.size())
        {
            if(jrm[i]<=jt)
            {
                ans-=2;
                jt-=jrm[i];
            }
            else break;
        }

        cout<<"Case #"<<l+1<<": "<<ans<<endl;
    }
}