#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>



using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int d,n;
        cin >> d >> n;
        double mx=0;
        for (int j=0;j<n;j++)
        {
            double curr,k,s;
            cin >> k >> s;
            curr = (d-k)/s;
            mx=max(mx,curr);
        }
        double sp=d/mx;
        printf("Case #%d: %0.6lf\n",i+1,sp);
        //cout << "Case #" << i+1 << ": " << sp << "\n";
    }



}
