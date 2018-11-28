#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

#define MAXN	20
int arr[MAXN];

int main()
{
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		string str;
		cin>>str;

		int N = str.length();

		for(int i=0;i<N;i++)
		{
			arr[i] = str[i]-'0';
		}

		int k=0;
		while(k<N-1 && arr[k]<=arr[k+1])
			k++;

		if(k==N-1)
		{
			cout<<"Case #"<<tc+1<<": "<<str<<endl;
		}
		else
		{
			int last = N;
			while(k>0)
			{
				arr[k]--;
				last = k;
				k--;
				if(arr[k]<=arr[k+1])
					break;
			}

			if(k==0 && arr[k]>arr[k+1])
			{
				arr[k]--;
				last = 0;
			}

			if(arr[0]==0)
			{
				cout<<"Case #"<<tc+1<<": ";
				for(k=1;k<N;k++)
				{
					cout<<"9";
				}
				cout<<endl;
			}
			else
			{
				cout<<"Case #"<<tc+1<<": ";
				for(k=0;k<=last;k++)
				{
					cout<<arr[k];
				}

				for(k=last+1;k<N;k++)
				{
					cout<<"9";
				}
				cout<<endl;
			}
		}
	}
	return 0;
}
