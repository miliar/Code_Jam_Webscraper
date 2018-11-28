#include <bits/stdc++.h>


using namespace std;



bool row[1000];
int n, k;

void read()
{
	string pancakes;

	cin>>pancakes;

	n = pancakes.length();
	for(int i = 0; i < n; ++i)
		row[i] = pancakes[i] == '+';
	
	cin>>k;

	return;
}


void solve()
{
	int result = 0;

	for(int i = 0; i <= n-k; ++i)
	{
		if(!row[i])
		{
			result++;
			for(int j = 0; j < k; ++j)
			{
				if(row[i+j])
					row[i+j] = 0;
				else
					row[i+j] = 1;
			}
		}
	}

	for (int i = n-k + 1; i < n; ++i)
	{
		if(!row[i])
		{
			cout<<"IMPOSSIBLE";
			return;
		}
	}
	cout<<result;
	return;

}



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;
	for(int t=1; t<= T; ++t)
	{
		read();	
		cout<<"Case #"<<t<<": ";
		solve();
		cout<<"\n";
	}


	return 0;
}