#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;

#define pb push_back

const double PI = 2 * acos(0);
const double eps = 1e-9;


class pancake{
	public:
	int R;
	int H;
	bool operator<(const pancake &a) const{
		if( R==a.R)
			H<a.H;
		else
			return R<a.R;	
	}

};
int N,K;
double dp[1000+1][1000+1];
vector<pancake> pans;
double solver(int n, int k)
{
	if(n<k)return -1;
	if(dp[n][k]>0)
		return dp[n][k];
	if(k==0)
	{
		//dp[n][k]=max(1.0*(fabs(PI*prev*prev -PI*pans[n].R*pans[n].R)+PI*pans[n].R*pans[n].R+2*PI*pans[n].R*pans[n].H) ,solver(n-1,k,prev));
		double max1=0;
		int idx=0;
		return PI*pans[n].R*pans[n].R+2*PI*pans[n].R*pans[n].H;
	}
	else if (n==0)
	{

		return PI*pans[n].R*pans[n].R+PI*pans[n].R*pans[n].R+2*PI*pans[n].R*pans[n].H;
	}
	else
	{
		//dp[n][k]=max(1.0*(fabs(PI*prev*prev -PI*pans[n].R*pans[n].R)+2*PI*pans[n].R*pans[n].H )+solver(n-1,k-1,pans[n].R) ,solver(n-1,k,prev));
		double max1=0;
		for (int i=n-1;i>=(k-1);i--)
		{
		   if(max1<solver(i,k-1) + (1.0*(fabs(PI*pans[n].R*pans[n].R -PI*pans[i].R*pans[i].R)+2*PI*pans[n].R*pans[n].H ))  )
			max1=solver(i,k-1) + (1.0*(fabs(PI*pans[n].R*pans[n].R -PI*pans[i].R*pans[i].R)+2*PI*pans[n].R*pans[n].H ));
		}
		dp[n][k]=max1;
		return dp[n][k];
	}

}
int main(int argc, char *args[]) {
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
	    scanf("%d %d",&N,&K);
	    for(int j=0;j<N;j++)
	    {
		    pancake tmp;
		    scanf("%d %d",&tmp.R,&tmp.H);
		    pans.pb(tmp);
	    }
	    sort(pans.begin(),pans.end());
	  /*  int idx[N+1];
	    idx[0]=0;
	    for(int j=0;j<N-1;j++)
	    {
		if(pans[j].R!=pans[j+1].R)
		{
			idx[j]=j+1;
		}
	    }*/
	    memset(dp,0,sizeof(double)*(1000)*(1000));
            double max1=0;
	    for(int j=0;j<N;j++)
		if(max1<solver(j,K-1))
			max1=solver(j,K-1);
	    double ts=-1;
	    printf("Case #%d: %.9f\n",i,max1);
	    pans.resize(0);
    }

	
    return 0;
}
