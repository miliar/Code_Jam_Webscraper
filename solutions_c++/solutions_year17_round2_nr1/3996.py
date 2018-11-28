#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int t,n;
	
	cin>>t;
	for(int ti=1;ti<=t;ti++)
	{
	    double k,d,min=0.0,m,s,ans;
	    cin>>d>>n;
	    for(int i=0;i<n;i++)
	    {
	        cin>>k>>s;
	        m=(d-k)/s;
	        if(m>min)
	            min=m;
	    }
	    ans=d/min;
	    cout << std::setprecision(100);
	    cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
	return 0;
}
