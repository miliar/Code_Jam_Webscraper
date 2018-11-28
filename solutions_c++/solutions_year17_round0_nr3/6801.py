#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int t,n,k,temp=1,x,y;
	int arr[2006];
	cin>>t;
	vector <int> q;
	while(t--)
	{
		cin>>n;
		
		cin>>k;
		//arr[0]=1;
		//arr[n+1]=1;
		x=0;
		y=0;
		q.clear();
		q.push_back(n);
		for(int i=0;i<k;i++)
		{	
			n=q.back();
			q.pop_back();
			if(n>0)
			{
			if(n%2==0)
			{
				x=n/2;
				y=(n/2)-1;
				
			}
			else
			{
				x=n/2;
				y=n/2;

			}
			q.push_back(x);
			q.push_back(y);
			
			
			
			
			}
			sort(q.begin(),q.end());
		}

		cout<<"Case #"<<temp<<": "<<x<<" "<<y<<"\n";
		temp++;



			

		



	}
	return 0;
}
