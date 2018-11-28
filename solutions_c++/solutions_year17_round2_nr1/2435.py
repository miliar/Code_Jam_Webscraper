#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <math.h>
#include <queue>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define RO(i,b,a) for (int i = (b); i >= (a); i--)
#define pb push_back
#define ARR0(A) memset((A), 0, sizeof((A)))
#define ARR1m(A) memset((A), -1, sizeof((A)))
#define ARR0(A) memset((A), 0, sizeof((A)))
#define ARRINF(A) memset((A), 10000, sizeof((A)))

/*
Why did ceil did not work?
*/


typedef long long LL;
using namespace std;


void Q20171(){
    int t,n; scanf("%d\n",&t);
    double d;

    FO(i,1,t+1)
    {   
        scanf("%lf %d\n",&d,&n);

        double k,s,tt=-1;
        vector<double> ks,ss;
        ks.clear();ss.clear();

        FO(j,0,n)
        {
            scanf("%lf %lf\n",&k,&s);

            tt = max(tt,(d-k)/s);
            ks.pb(k);ss.pb(s);

        } 

        double maxd = d;
        FO(j,0,n)
        {
            maxd = min(maxd,ks[j]+ss[j]*tt);
        }
        double sol = maxd/tt;
        printf("Case #%d: %lf\n",i,sol);

    }

}

int main()
{   
    Q20171();
    
    return 0;
}
