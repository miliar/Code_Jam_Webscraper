#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<cstdint>
#include <algorithm>
#include <unordered_map>
using namespace std;
#include <bits/stdc++.h>



int main()
{
   
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++)
	{
		int n,i;
        double d,maxx=-1000;
        cin>>d>>n;
        double km[n],speed[n];
         for(i=0;i<n;i++)
            { 
             cin>>km[i]>>speed[i];
            maxx=max(maxx,((d-km[i])/speed[i]));
         //    cout<<maxx<<"\n";
         }
      
        double ans=d/maxx;
        //if(ceil(ans)==floor(ans))
         //   ans=ans+0.000000;
        cout << "Case #" << tt << ": ";
        cout<<std::setprecision(6)<<std::fixed<<ans<<"\n";
		
	}
    return 0;
}
  