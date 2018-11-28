#include <bits/stdc++.h>
using namespace std;
#define ll long long int

/*template<typename T> void print_queue(T q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}*/

int main()
{
	ll t,n,k;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		ll val,x,y;
		cin>>n>>k;
		priority_queue <ll> q,fu;
		q.push(n);
		for(int i=0;i<k-1;i++)
		{
			val = q.top() - 1;
			//cout<<i<<": ";
			x = val/2;
			y = val-x;
			q.pop();
			q.push(x);
			q.push(y);
			//print_queue(q);
		}
		val = q.top() - 1;
		cout<<"Case #"<<z<<": ";
		cout<<max(val/2,val - (val/2))<<" ";
		cout<<min(val/2,val - (val/2))<<endl;
	}
	return 0;
}