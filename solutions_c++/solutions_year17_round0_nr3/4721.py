/*input
1
1 1
*/
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false);
	int test, z;
	cin>>test;
	for(z = 1; z <= test; z++)
	{
		cout<<"Case #"<<z<<": ";
		long long int n, k, top;
		cin>>n>>k;
		priority_queue<long long int > P;
		P.push(n);
		k--;
		while(k)
		{
			top = P.top();
			// cout<<"k : "<<k<<" top : "<<top<<endl;
			P.pop();
			if(top & 1) 
			{
				P.push(top/2);
				P.push(top/2);
			}
			else
			{
				P.push((top/2) - 1);
				P.push(top/2);
			}
			k--;
		}
		top = P.top();
		// cout<<"finally top : "<<top<<endl;
		if(top & 1)
		{
			cout<<top/2<<" "<<top/2<<endl;
		}
		else
		{
			cout<<(top/2)<<" "<<(top/2 - 1)<<endl; 
		}

	}
		
	return 0;
}