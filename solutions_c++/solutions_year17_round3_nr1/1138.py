#include<iostream>
#include<cstdio>
#include<numeric>

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


const double PI  =3.141592653589793238463;



int main()
{
	int t;
	cin>>t;


	for (unsigned csn=1;csn<=t;csn++)
	{
        int n,k;
        cin>>n>>k;
        vector<pair<long long,long long> > pan(n);
        vector<long long> weight(n);

        for (int i=0;i<pan.size();i++)
            {
                cin>>pan[i].first>>pan[i].second;
            }

        sort(pan.begin(),pan.end());
        for (int i=0;i<weight.size();i++)
            weight[i]=2*pan[i].first*pan[i].second;
        long long test=0;
        for (int i=pan.size()-1;i>=0 && i>=k-1;i--)
        {
            long long ans=weight[i]+pan[i].first*pan[i].first;

            if( i>0)
            {

            vector<long long> temp(weight.begin(),weight.begin()+i);
            sort(temp.begin(),temp.end());
            reverse(temp.begin(),temp.end());
            ans=accumulate(temp.begin(),temp.begin()+k-1,ans);
            }
            test=max(test,ans);



        }

        printf("Case #%d: %.9lf\n",csn,PI*test);
		//cout<<"Case #"<<csn<<": "<<(PI*test) <<endl;
	}

	return 0;
}
