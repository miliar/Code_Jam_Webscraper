#include<iostream>
#include<string>
using namespace std;
bool check(int N)
{
	if(N%10==0)
	{
		return false;
	}
	else{
		bool ch=true;int m;
		while(N>0 && ch)
		{
			int m=N%10;
			N=N/10;
			if(m >= N%10)
			{
				ch =true;
			}
			else
			{
				ch = false;
				break;
			}
		}
		return ch;
	}
}
int main()
{
	int t,n,latest;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		cin>>n;
	    latest=1;
		for(int i=1;i<=n;i++)
		{	
			if(check(i))
			{
			    latest=i;
			}
		}
	cout << "Case #" << j+1 << ": " << latest << endl;
	}
	
}
