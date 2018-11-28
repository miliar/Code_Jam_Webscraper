#include<bits/stdc++.h>

using namespace std;

long long int tidy_num(long long int n)
{
	while(true)
	{
		int flag=0;
	//	if(n%10==0)
	//	{
	//	 n--;
	//	}
		 if(n<10)
		{
			return n;
		}
		else
		{
			long long int temp = n;
			int t1 = temp%10;
			while(temp>0)
			{
				
				temp = temp/10;
				int t2 = temp%10;
				
				if(t1<t2)
				{
				flag=1;	
				n--;
				break;
				}
				t1=t2;
				
			}
			
			if(flag==0)
			{
			
			return n;
			break;
	}
		}
		
	}
}

int main()
{
	long long int n;
	int t;
	
	
	
	ifstream cin("C:/Users/Prashant Pratap/Desktop/B-small-attempt0.in");
    ofstream cout("C:/Users/Prashant Pratap/Desktop/out.txt.txt");
	cin>>t;
	int c=1;
	while(t--)
	{
		cin>>n;
		long long int ans = tidy_num(n);
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
	}
	return 0;
}
