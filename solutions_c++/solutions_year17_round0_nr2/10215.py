#include<iostream>
#include<cmath>

#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<string>

#include<algorithm>

using namespace std;

bool isnice(int n)
{
	int max = n%10;

	while(n)
	{
		if(max < n%10)
			return false;
		else
		{
			max = n%10;
			n = n/10;
		}
	}
	return true;
}
int main()
{
	
	int t, n;

	cin>>t;
	for(int i = 0; i < t; i++)
	{
		cin>>n;

		while(n)
		{
			if(isnice(n))
			{
				cout<<"Case #"<<i+1<<": "<<n<<"\n";
				break;
			}
			n--;
		}
	}
	return 0;
}

