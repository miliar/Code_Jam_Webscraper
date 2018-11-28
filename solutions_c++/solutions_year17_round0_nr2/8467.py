#include <bits/stdc++.h>

using namespace std;

bool sol(long long int N)
{
	int precedente = 9;
	
	while(N != 0)
	{
		if(N%10 > precedente)
			return false;
		precedente = N%10;
		
		N = (N - N%10)/10;
	}
	
	return true;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.in", "w", stdout);

	int T;
	cin >> T;
	
	for(int i = 0; i < T; i++)
	{
		long long int N;
		cin >> N;
		
		for(long long int j = N; j >= 1; j--)
		{
			if(sol(j))
			{
				cout << "Case #" << i+1 << ": " << j << endl;
				break;
			}
		}
	}
}
