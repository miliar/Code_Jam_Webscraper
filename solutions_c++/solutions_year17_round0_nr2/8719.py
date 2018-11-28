#include<iostream>
using namespace std;
int main()
{
	long long int n;
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		long long int tidy=1;
		for(long long int w=1;w<=n;w++)
		{
			if(w<10)
				tidy=w;
			else
			{
				long long int tmp=w;
				int g,h;
				do
				{
					g=tmp%10;
					tmp=tmp/10;
					if(tmp!=0)
					{
						h=tmp%10;
						if(g<h)
							break;
					}
				}while(tmp!=0);
				if(g>=h)
					tidy=w;
			}
		}
		cout<<"Case #"<<i<<": "<<tidy<<endl;
	}
	exit(0);
}
