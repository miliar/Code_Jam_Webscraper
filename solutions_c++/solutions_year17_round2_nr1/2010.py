#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	int j = 1;
	while(t--)
	{
	    int D,N;
	    double cost = 0;
	    cin>>D>>N;
	    for(int i=0;i<N;i++)
	    {
	        double K,S;
	        cin>>K>>S;
	        double temp = (D-K)/S;
	        if(temp > cost)
	        cost = temp;
	    }
	    double ans = ((double)D)/cost;
	    cout<<"Case #"<<j++<<": "; 
	    printf("%.6lf\n",ans);
	}
	return 0;
}
