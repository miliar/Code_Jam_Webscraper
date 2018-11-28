#include <bits/stdc++.h>
#define l long int
#define ll long long int
#define ull unsigned long long int

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ull t,i=1;
	cin>>t;
	while(i<=t)
	{
		ull flag=0;
		ull n,k;
		cin>>n>>k;
		//cout<<"for n= k="<<n<<"  "<<k<<endl;
		priority_queue<int> q;
		if(n==k)
		{
			cout<<"Case #"<<i<<": "<<0<<" "<<0<<endl;
		}
		else if(k==1)
		{
			//cout<<"n=k="<<n<<k<<endl;
			if(n%2==0)
			{
				ull max=n/2;
				ull min=(n/2)-1;
				cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;
			}
			else
			{
				cout<<"Case #"<<i<<": "<<n/2<<" "<<n/2<<endl;
			}
		}
		else
		{
			if(n%2==0)
			{
				q.push(n/2);
				q.push((n/2)-1);
			}
			else
			{
				q.push(n/2);
				q.push(n/2);
			}
			while(k--)
			{
				ull x=q.top();
				//cout<<"top "<<x<<endl;
				q.pop();
				if(k!=1)
				{
					if(x%2==0)
					{
						q.push(x/2);
						q.push((x/2)-1);
					}
					else
					{
						q.push(x/2);
						q.push(x/2);
					}	
				}
				if(k==1)
				{
				
					//cout<<"hey x="<<x<<endl;
					if(x%2==0)
					{
						ull max=(x/2);
						ull min=(x/2)-1;
						cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;
						break;
					}
					else
					{
						ull max=x/2,min=x/2;
						cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;
						break;
					}

				}
			
			}
		

		}

	
		i++;
	}
	return 0;
}