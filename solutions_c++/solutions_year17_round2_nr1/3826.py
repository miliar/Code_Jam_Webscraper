#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    	freopen("input.cpp","r",stdin);
	freopen("output.cpp","w",stdout);
    int t,test;
    cin>>t;
    for(test=1;test<=t;test++)
    {
        double d,n,tt,dist;
        cin>>d>>n;
        double maxt=0;
        for(double i=0;i<n;i++)
        {
            double k,s;
            cin>>k>>s;
            dist=d-k;
            tt=dist/s;
            maxt=max(maxt,tt);

        }
        double ans=d/maxt;
       printf("Case #%d: %.6lf\n",test,ans);
    }
    fclose(stdout);
    return 0;
}
