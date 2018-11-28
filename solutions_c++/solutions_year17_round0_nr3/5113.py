#include <iostream>
#include <queue>

using namespace std;

void solve()
{
	int n, k;
	cin>>n>>k;
	int l, r;
	priority_queue<int> pq;
	pq.push(n);
	int x;
	for(int i=0; i<k; i++) 
	{
		x = pq.top(); pq.pop();
		l = (x-1)/2;
		r = x/2;
		if(l) pq.push(l);
		if(r) pq.push(r);
	}
	cout<<r<<" "<<l<<endl;
}

int main()
{
	int T;
	cin>>T;
	for(int i=1; i<=T; i++) 
	    cout<<"Case #"<<i<<": ",
		solve();
	return 0;
}