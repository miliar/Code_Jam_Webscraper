#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int E[100];
int S[100];
int D[100][100];
double mintime[100];

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N, Q;
		cin >> N >> Q;
		
		for (int i = 0; i < N; i++)
			cin >> E[i] >> S[i];

		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				cin >> D[i][j];
		
		for (int q = 0; q < Q; q++)
		{
			int U, V;
			cin >> U >> V;
		}

		for (int i = 0; i < N; i++)
			mintime[i] = 0.0;
		
		for (int i = 1; i < N; i++)
		{
			long long int dist = 0;

			for (int j = i - 1; j >= 0; j--)
			{
				dist += D[j][j+1];
				if (E[j] >= dist)
				{
					double new_mintime = mintime[j] + dist / (double)S[j];
//					cerr << i << " " << j << ": " << new_mintime << "\n";
					if (mintime[i] == 0.0 || mintime[i] > new_mintime)
						mintime[i] = new_mintime;
				}
			} 
//			cerr << i << ": " << mintime[i] << "\n";
		}
		
		cout.precision(17);
		cout << "Case #" << t << ": " << mintime[N-1] << "\n";
	}
	
	return 0;
}

