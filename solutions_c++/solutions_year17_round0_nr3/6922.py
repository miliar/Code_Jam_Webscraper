#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

void solve(int a)
{
	vector<long long> intervals;
	long long t,p;
	cin>>t>>p;
	long long max = t;
	long long min = t;
	intervals.push_back(max);
	long long diff = t-p;
	long long po = (long long) floor(log2(p));
	diff/=pow(2,po);
	max = (diff+1) / 2;
	min = (diff+1) / 2 -1 + (diff+1)%2;
	
	cout<<"Case #"<<a<<": ";
	cout<<max<<" "<<min<<endl;
}

int main()
{
	int tests;
	cin>>tests;
	for (int i = 0;i<tests;i++) solve(i+1);
	return 0;
}
