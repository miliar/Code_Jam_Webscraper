#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long t;
    cin>>t;
    for(long long i = 0;i< t;i++)
    {
        long long d,n;
        cin>>d>>n;
        double maxi = 0;
        while(n--)
        {
            long long k,s;
            cin>>k>>s;
            long long dist = d-k;
            double t = (double)dist/s;
            if(t > maxi)
                maxi = t;

        }
        printf("Case #%lld: %.6lf\n",i+1,(d)/maxi);
    }
}
