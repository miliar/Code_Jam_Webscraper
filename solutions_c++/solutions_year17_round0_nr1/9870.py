#include <bits/stdc++.h>
typedef long long int xxl;
using namespace std;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false);
	int t,su;

	cin >> t;
	for (int ii = 0; ii < t; ++ii)
	{
		string a;
		int k;
		cin >>a;
		cin >>k;
		bool check=false;
		for (int i = 0; i < a.size(); ++i)
		{
			if(a[i]=='-')
				break;
			if(i==a.size()-1)
			{
				check=true;
				
				break;
			}
		}
		if(check)
		{
			cout << "Case #"<<ii+1<<": "<<0<< endl;
			continue;
		}

		int sum=0;
		for (int i = 0; i < a.size()-k+1; ++i)
		{
			if(a[i]=='-')
			{
				sum++;
				for (int j = i; j < i+k; ++j)
				{
					a[j]=(a[j]=='-')?'+':'-';
				}
			}
		}

		for (int i = 0; i < a.size(); ++i)
		{
			if(a[i]=='-')
			{
				check=true;
				break;	
			}
		}	
		if(check)
		{
				cout << "Case #"<<ii+1<<": IMPOSSIBLE"<< endl;
		}		
		else
			cout << "Case #"<<ii+1<<": "<<sum<< endl;
	}
	return 0;
}

//i+k-1

