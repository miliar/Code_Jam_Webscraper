#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("c-small.txt","r",stdin);
	freopen("k2.txt","w",stdout);
	int t,t1;
	cin>>t;
	t1=t;
	while(t--)
	{
		
		long long int n,k;
		int i,j,z,mm=0;
		cin>>n>>k;
		cout<<"Case #"<<t1-t<<": ";
		if(k>n)
		cout<<"0 0\n";
		else
		{
			priority_queue<int> q;
			q.push(n);
			while(k>1)
			{
				k--;
				long long int z=q.top();
				if(z==1&&k>1)
				break;
				if(z%2==0)
				{
					q.pop();
					q.push(z/2);
					q.push(z/2-1);
					
				}
				else
				{
					q.pop();
					q.push(z/2);
					q.push(z/2);
				}
			}
			if(k>1)
			cout<<"0 0\n";
			else
			{
				z=q.top();
				if(z%2==0)
				cout<<z/2<<" "<<z/2-1<<endl;
				else
				cout<<z/2<<" "<<z/2<<endl;
			}
			
		}
		
	}
	return 0;
	
}
