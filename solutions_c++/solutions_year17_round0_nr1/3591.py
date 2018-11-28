#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

#define MAXN	1001
int arr[MAXN];

int main()
{
	int T;
	cin>>T;

	for(int tc=0;tc<T;tc++)
	{
		string s;
		cin>>s;
		
		int N = s.length();
		int i;
		for(i=0;i<N;i++)
		{
			if(s[i]=='+')
				arr[i] = 1;
			else
				arr[i] = 0;
		}

		int K;
		cin>>K;

		int flips=0;
		i=0;

		while(i<N)
		{
			while(i<N && arr[i]==1)
				i++;
			if(i<N)
			{
				if((i+K-1)>=N)
				{
					flips = -1;
					break;
				}
				else
				{
					flips++;
					for(int k=i;k<i+K;k++)
					{
						arr[k] ^= 1;
					}
					i++;
				}
			}
		}

		if(flips==-1)
			cout<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<tc+1<<": "<<flips<<endl;
	}

	return 0;
}