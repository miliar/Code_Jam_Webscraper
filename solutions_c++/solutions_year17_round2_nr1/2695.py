/*input
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
*/
#include <bits/stdc++.h>
using namespace std;
 
#define lli long long int
#define mod 1e9+7
#define f(i,x,n) for(i=x;i<n;i++)
#define vlli vector<lli>
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

int main(int argc, char const *argv[])
{
    // ios_base::sync_with_stdio(false);
    int test, z;
    scanf("%d", &test);
    for(z = 1; z <= test; z++)
    {
    	printf("Case #%d: ", z);
    	// cout<<"Case #"<<z<<": ";
    	lli d, n;
    	scanf("%lld", &d );
    	scanf("%lld", &n );
    	double dist, time;
    	double maxx = 0;
    	// vector<double> k(n), s(n);
    	for (int i = 0; i < n; ++i)
    	{
    		scanf("%lf", &dist);
    		scanf("%lf", &time);
    		double t = (d - dist)/time;
    		if( t > maxx )
    			maxx = t;
    		/* code */
    	}

    	if(maxx == 0)
    		printf("%.12lf\n", 0.0);
    	else
    	{	
    		double ans = double(d)/maxx;
    		printf("%.12lf\n", ans);
    	}

    }
    return 0;
}
