#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	for(int i=1;i<=t;i++)
	{
	    int f,n;
	    double temp1,temp2;
	    cin>>f>>n;
	    double maxt=-1.00000000f,tf=0.00000000f;
	    vector<int> horse;
	    for(int j=0;j<n;j++)
	    {
	        cin>>temp1>>temp2;
	        tf=(f-temp1)/temp2;
	        if(tf>maxt)
	        {
	            maxt=tf;
	        }
	    }
	    printf("Case #%d: %.8f\n",i,f/maxt);
	    //cout<<"Case #"<<i<<": "<<setprecision(9)<<(f/maxt)<<"\n";
	}
	return 0;
}
