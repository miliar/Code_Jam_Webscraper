#include <iostream>
#include <string>
using namespace std;

int inverse(string s, long int k,int count) 
{
	int z = 0,x=0;
		while(s[z] != '\0')
		{
			if(s[x]== '-')
			{
				count ++;
				if(s.length()- x < k)
				{
					return -1;
				}

				for(int j = x; j < x+k ; j++)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
			x++;
			z++;
		}
	return count;
}

int main()
{
	int t;
	string s;
	long int k;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		long int count=0;
		cin>>s;
		cin>>k;
		count=inverse(s,k,count);
		if(count == -1)
		{
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else
			cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	return 0;
}