#include <iostream>
#include<cmath>
#include<vector>
using namespace std;

int main() { std::cout << std::fixed;
	cout.precision(6);
	long long int d;
	cin>>d;
	long long int n;
	cin>>n;
	vector<long long int> starting(n);
	vector<double> speed(n);
	for(long long int i =0;i<n;i++)
	cin>>starting[i]>>speed[i];
	
	double mx=(d-starting[0])/speed[0];
	for(long long int  i=1;i<n;i++)
	mx=max(mx,(d-starting[i])/speed[i]);
	
	double ans=d/mx;
	
	cout<<ans<<endl;
	
	// your code goes here
	return 0;
}