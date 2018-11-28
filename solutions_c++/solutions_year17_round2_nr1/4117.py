#include <iostream>
#include<algorithm>
#include<cmath>
#include<iomanip>
using namespace std;

int main() {
	int t,x=1;
	cin>>t;
	while(t--)
	{
		double k,m;
	    long long d,a,b;
	    cin>>k>>d;
	    m=0;
	    for(int i=0;i<d;i++)
	    {
	        cin>>a>>b;
	        m=max(m,(k-a)/b);  
	    }
	    cout<<"Case #"<<x<<":"<<" ";
	    cout<<fixed<<setprecision(6)<<k/m<<endl;
	    x++;
	}
	return 0;
}

