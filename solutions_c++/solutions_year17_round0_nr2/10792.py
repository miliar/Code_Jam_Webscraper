#include <iostream>
using namespace std;

int checktidy(int N)
{
	int tidy = 1;
	int T = N%10;

	while(N!=0 && tidy!=0)
	{
		T = N%10;
		N = N/10;
		if(T>=N%10)
			tidy = 1;
		else tidy = 0;
	}

	return tidy;
}

int main(int argc, char const *argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output","w",stdout);
	int T,N,tidyno = 1;
	cin>>T;
	int arr[T];
	for (int i = 1; i <= T; ++i)
	{
		cin>>arr[i-1];
	}
	for (int i = 0; i < T; ++i)
	{
		for(int j=1;j<=arr[i];j++)
		{
			if(checktidy(j)==1)
			{
				tidyno = j;
			}
			else continue;
		}

		cout<<"Case #"<<i+1<<": "<<tidyno<<"\n";
	}


	return 0;
}


