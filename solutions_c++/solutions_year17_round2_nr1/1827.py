#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>
using namespace std;

#define ll long long
#define inf 1e18
int main() 
{
      freopen("input2.in", "r", stdin);
      freopen("output2.txt", "w", stdout);  
    int n,t;
    double max,k,s,ans,d;
    cin>>t;
    for(int k_=1;k_<=t;k_++)
    {
        cin>>d>>n;
        max=0;
        while(n--)
        {
            cin>>k>>s;
            if((d-k)/s > max)
            max=(d-k)/s;
        }
        ans=d/max;
        
        cout<<"Case #"<<k_<<": ";
        printf("%.6lf\n",ans);
    }
    return 0;
}
