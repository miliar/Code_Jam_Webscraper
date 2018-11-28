#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <sstream>  // Required for stringstreams

using namespace std;
typedef   long long ll;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outputcodeA.txt", "w", stdout);

    int cases = 0 ;
    cin>>cases;
    for (int kk = 1; kk<cases+1; kk++) {
        double a,b,x,y,n,vit;
        double xx=0,yy=0;
        cin>>a>>n;
        double reste = 0 ;
        for (int i=0; i<n ; i++) {
            
            cin>>x>>vit;
            reste=a-x;
            if (xx<(reste/vit)) {
                xx=reste/vit;
            }
        }
        //cout<<xx<<endl;
     printf("Case #%d: %f\n",kk,a/xx);

    }
    
    
    return 0;
}

