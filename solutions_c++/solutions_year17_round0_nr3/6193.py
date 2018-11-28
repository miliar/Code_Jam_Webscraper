#include <iostream>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

#define CLR(a,x) memset(a,x,sizeof a)
#define LL long long
#define LD  long double
#define ALL(v) v.begin(),v.end()
#define FR(i,n) for(LL i=0;i<(LL)n;i++)
#define FAB(i,a,b) for(LL i=(LL)a;i<(LL)b;i++)
#define FBA(i,b,a) for(LL i=(LL)b;i>=(LL)a;i--)
#define IIN(x) scanf("%d",&x)
#define IIN2(x,y) scanf_s("%d%d",&x,&y)
#define LIN(x) scanf_s("%I64d",&x)
#define LIN2(x,y) scanf_s("%I64d%I64d",&x,&y)
#define EXIT(n) {cout<<n<<endl;return 0;}
#define PII pair<LL,int>
#define PPI pair<PII,int>
#define PPP pair<PII,PII>
#define PLL pair<LL,LL>
#define PPL pair<LL,PLL>
#define PDD pair<double,double>
#define PDI pair<double,int>
#define PIS pair<int,string>
#define PSI pair<string,int>
#define BIT(mask,i) ((mask>>i)&1)
#define PI 3.141592653589793238
#define VI vector<int>
#define VPI vector<PII>
#define VLL vector<LL>
#define VPL vector<PLL>
#define VS vector<string>
#define VVI vector<VI>
#define SI multiset<int>
#define SLL set<LL>
#define SLP set<PPL>
#define SPI set<PII>
#define SS set<string>
#define MII map<int,int>
#define MLL map<LL,LL>
#define MIP map<int,PII>
#define MSI map<string,int>
#define MSL map<string,LL>
#define MIS map<int,string>
#define INF 2000000000000000000
#define MOD (1000*1000*1000+7)
#define MAX (1000*1000+10)

int t,cnt[MAX];


int main()
{
    cnt[1]=cnt[2]=1;
    FAB(i,3,MAX)
    {
        if(i&1) cnt[i]=cnt[i/2]*2;
        else cnt[i]=cnt[i/2]+cnt[i/2-1];
    }
    
    cin>>t;
    FR(q,t)
    {
        SI s;

        int n,k,mn,mx;
        cin>>n>>k;
        
        if(k>n-cnt[n]) mx=mn=0;
        else
        {
            s.insert(n);
            FR(i,k)
            {            
                SI::iterator it=s.end(); it--;
                int x=(*it);
                mn=x/2; mx=x/2;
                if(x==mx+mn) mn--;
                s.erase(it);
                if(mx>1) s.insert(mx);
                if(mn>1) s.insert(mn);
            }
        }
        cout<<"Case #"<<q+1<<": "<<mx<<" "<<mn<<endl;
    }

	return 0;
}
