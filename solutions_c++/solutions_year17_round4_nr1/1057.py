#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void doCase()
{
	int N; 
	cin >> N;
	int P;
	cin >> P;
	int *G = new int[P];
	for (int i = 0; i < P; i++)
		G[i] = 0;
	for (int i = 0; i < N; i++)
	{
		int g;
		cin >> g;
		G[g%P]++;
	}

	if(P == 2)
	{
		int result = G[0] + G[1] / 2;
		if ((G[1] % 2) != 0)
			result++;
		cout << result << endl;
	}
	else if (P == 3)
	{
		int result = G[0];
		int minv = std::min(G[1], G[2]);
		result += minv;
		G[1] -= minv;
		G[2] -= minv;
		result += G[1] / 3;
		result += G[2] / 3;
		if ((G[1] % 3) != 0 || (G[2] % 3) != 0)
			result++;
		cout << result << endl;		
	}
	else if (P == 4)
	{
		int result = G[0];
		int minv = std::min(G[1], G[3]);
		result += minv;
		G[1] -= minv;
		G[3] -= minv;
		int twos = G[2] / 2;
		result += twos;
		G[2] -= 2 * twos;
		if (G[2] >= 1 && G[1] >= 2)
		{
			result++;
			G[2] -= 1;
			G[1] -= 2;
		}
		int four1s = G[1] / 4;
		result += four1s;
		G[1] -= 4 * four1s;
		int four3s = G[3] / 4;
		result += four3s;
		G[3] -= 4 * four3s;
		if (G[1] > 0 && G[2] > 0 && G[3] > 0)
			result++;
		cout << result << endl;
	}

	delete[] G;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		doCase();
	}
}

