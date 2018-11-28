/*
    Just For You 97116:)
*/

#include <bits/stdc++.h>
using namespace std;

//important constants
#define pi M_PI
#define mod 1000000007
#define maX(a,b)        ((a)>(b)?(a):(b))
#define miN(a,b)        ((a)<(b)?(a):(b))

inline bool cmp (const pair<int,int> &a, const pair<int,int> &b){
    if (a.first != b.first)
        return a.first > b.first;
    return a.second < b.second;
}

int main()
{
	freopen("input.txt","r",stdin);
    // freopen("pA_1B_17output_samll.txt","w",stdout);
    freopen("pA_1B_17output_large.txt","w",stdout);
    int t,n,m,k,l,x,y,z,flag,count,sum,d,mx,mn,prod;
    double dist,ans,ret;

    vector< pair<double,double> > v;

    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
    	scanf("%d%d",&d,&n);
    	for(int i=0;i<n;i++){
        	scanf("%d%d",&x,&y);
        	v.push_back(make_pair(x,y));
    	}
    	
		ret = 0;
    	for(int i=n-1;i>=0;i--){
    		dist = (double)(d-v[i].first)/v[i].second;
    		if(dist>ret)
    			ret = dist;
    	}
    	ans = (double)d/ret;
    	printf("Case #%d: %lf\n",tt,ans);
    	v.clear();
    }
    return 0;
}