#include<bits/stdc++.h>
using namespace std;

void solve(string s)
{
	int n = s.length();

	string temp , init;

	int idx = -1;

	for(int i = 0 ; i < n ; i++)
		temp = temp + "1";

	for(int i = 1 ; i < n ; i++)
	{
		if( s[i] < s[i-1])
		{
			idx = i - 1;
			break;
		}
		temp[i-1] = s[i-1];
	}

	init = temp;

	for(int i = n - 1 ; i >= idx ; i--)
	{
		while( temp < s and (temp[i] - '0') != 9)
		{
			temp[i]++;
			if(temp > s)
			{
				temp[i]-- ;
				break;
			}

		}
	}

	if(temp == init )
	{
		if(temp == "1")
			cout<<"1";
		else
			for(int i = 0 ; i <(n - 1) ; i++)
				cout<<'9';
	}
	else
	{
		while(idx > 0)
		{
			while(temp[idx] < temp[idx - 1])
				temp[idx-1]--;

			idx--;
		}

		for(int i = n - 1 ; i >=0 ; i--)
		{
			while(temp < s and temp[i] != '9' )
				temp[i]++;

			if(temp > s)
				temp[i]--;
		}

		for(int i = 0 ; i < temp.length() ; i++)
			cout<<temp[i];
	}
	cout<<endl;

}

int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	int t;
	cin>>t;

	for(int i = 1 ; i <= t ; i++)
	{
		string num;
		cin>>num;
		cout<<"Case #"<<i<<": ";
		solve(num);

	}

	return 0;
}
