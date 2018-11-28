#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long ull;

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		string N;
		cin >> N;
		
		int i = 0; 
		while (i < N.size() - 1)
		{
			if (N[i] > N[i+1])
			{
				while (i > 0 && N[i-1] == N[i])
					i--;
				N[i] = N[i] - 1;
				for (int j = i + 1; j < N.size(); j++)
					N[j] = '9';
				break;
			}
			i++;
		}
		
		if (N[0] == '0')
			N = N.substr(1);
			
		cout << "Case #" << t << ": " << N << "\n";
	}
	
	return 0;
}

