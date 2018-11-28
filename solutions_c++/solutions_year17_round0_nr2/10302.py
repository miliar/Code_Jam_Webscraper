#include <bits/stdc++.h>

using namespace std;

bool isTidy(string S)
{
	for(int i = S.size() - 1; i > 0; i--)
	{
		if(S[i - 1] > S[i])
		{
			return false;
		}
	}
	return true;
	
	}

int main()
{
	int T;
	cin >> T;
	for(int x = 1; x <= T; x++)
	{
		long long int N;
		cin >> N;
		string S;
		
		while(N >= 0)
		{
			S = to_string(N);
			if(isTidy(S))
			{
				break;
			}
			N--;
		}
		
		cout << "Case #" << x << ": " << N << endl;
	}
	return 0;

}