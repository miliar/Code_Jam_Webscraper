#include<iostream>
#include<fstream>
using namespace std;
bool check(long long int n)
{
	while(n!=0)
	{
		int prev=n%10;
		int next=(n/10)%10;
		if(prev >= next)
		  {
		  	n/=10;
		  	continue;
		  }
		  else
		  return false;
	}
	return true;
}
int main()
{
	//FILE *in_file  = fopen("B-small-attempt1.in", "r");
	freopen("B-small-attempt2.in", "r", stdin);
freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	//fscanf(in_file, "%d", &t); 
	for(int i=1;i<=t;i++)
	{ int count=0;
	   int number;
		long long int n;
		cin>>n;
		//fscanf(in_file, "%lld", &n); 
		while(n>0)
		{ 
			if(check(n))
			{count=1;
			number=n;
			break;
			}
			else 
			{
			n--;
			continue;
		
	    	}
			
		}
		if(count==1)
		   cout<<"Case #"<<i<<": "<<number<<endl;
		  
	}
	return 0;
}
