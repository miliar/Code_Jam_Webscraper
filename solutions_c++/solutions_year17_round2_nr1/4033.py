#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>

#define pb push_back
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	int T,i,k,d;
	double m,a,b;
	cin>>T;
	for(i=1;i<=T;i++)
	{
	   double k,d;
	   cin>>k>>d;
	   m=0;
	   while(d--)
	   {
	       cin>>a>>b;
	       m=max(m,(k-a)/b);
	   }
	   cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<k/m;
	   cout<<"\n";
	}
	return 0;
}

