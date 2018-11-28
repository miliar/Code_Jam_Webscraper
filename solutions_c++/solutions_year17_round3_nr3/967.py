#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
#include<climits>
#define REP(i,a) for(int i=0;i<(a);++i)
#define SIZE(X) ((int)(X.size()))
#define PRN(X) REP (i,SIZE(X)) cout<<X[i]<<" ";
#define RV(X) REP (i,SIZE(X)) cin>>X[i];
using namespace std;
template <class it> void  itover(it begin, it end){ if(begin!=end)cout<<*(begin++);for(;begin!=end;begin++)cout<<" "<<*begin;}
template<class t1,class t2> ostream &operator << (ostream &os, pair<t1,t2> p ) {os<<"("<<p.first<<","<<p.second<<")";return os;}
typedef long long int64;
typedef long long ll;
const int inf=INT_MAX;
const ll infl=LLONG_MAX;






int main()
{
	int t;
	cin>>t;
	for (unsigned csn=1;csn<=t;csn++)
	{
        int n,k;
        cin>>n>>k;
        double u;
        cin>>u;
        vector<double> p(n);
        vector<double> diff(n);

        RV(p);
        double ans=0;
        if(n >1)
        {
        sort(p.begin(),p.end());
        diff[0]=p[1]-p[0];

        ans=1.0;
        double low=p[0];
        int index=-1;
        for (int i=0;i<p.size()-1 && u>0;i++)
        {
            diff[i]=p[i+1]-p[i];
            if((i+1)*diff[i]<=u   )
            {
                u-=(i+1)*diff[i];
                low=p[i+1];
                index=i;
            }
            else
                {
                low=p[i]+u/(i+1);
                    u=0;

                    index=i;

                }
                //cout<<u<<" "<<low<<endl;

        }
        if (u > 0)
        {
                low=p.back()+u/n;
                ans=pow(low,n);
        }
        else
        {
        for (int i=0;i<p.size();i++)
        {
                if(i<=index)
                    ans*=low;
                    else
                    ans*=p[i];
        }
        }
        }
        else
            ans=p[0]+u;

		printf("Case #%d: %.9lf\n",csn,ans);

	}

	return 0;
}
