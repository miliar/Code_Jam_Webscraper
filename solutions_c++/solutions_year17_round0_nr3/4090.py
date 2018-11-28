#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	long long int t,n=0,k=0,x=0;
	long long int nm;
	long long int  mx, mn;

	cin>>t;

	for(x=1; x<=t; x++)
	{
		cin>>n;
		cin>>k;

		priority_queue<long long int> qu;
		qu.push(n);

		for(int i=0; i<k; i++)
		{
			nm = qu.top();
			qu.pop();
			mn = nm - nm/2 - 1;
			mx = nm/2;
			qu.push(mn);
			qu.push(mx);
		 }
		cout<<"Case #"<<x<<": "<<mx<<" "<<mn<<"\n";
	}
	return 0;
}

