#include <iostream>
#include <fstream>

using namespace std;

int min(int a, int b)
{
	if (a >= b) return b;
	else return a;
}

int max(int a, int b)
{
	if (a <= b) return b;
	else return a;
}

int main()
{
	int T;    //cases
	int N;    //number of stalls
	int K;    //number of enter
	int i = 1;//counter
	int counter = 1;
	int left, right; //current position
	int currMin=0, currMax=0;
	int currPosition = 0;
	int minimal, maximal;
	int x, y; //finish position
	ifstream fin("C-small-1-attempt1 (1).in");
	ofstream fout("Output.out");
	fin >> T;
	while (i <= T)
	{
		fin >> N;
		fin >> K;
		int *Array = new int[N + 2];
		Array[0] = 1;
		Array[N + 1] = 1;
		for (int j = 1; j <= N; j++)
		{
			Array[j] = 0;
		}
		while (counter <= K)
		{
			for (int k = 1; k < N + 1; k++)
			{
				if (Array[k] == 0)
				{
					int z = 1;
					while (true)
					{
						if (Array[k - z] == 1)
						{
							left = z - 1;
							break;
						}
						z++;
					}
					z = 1;
					while (true)
					{
						if (Array[k + z] == 1)
						{
							right = z - 1;
							break;
						}
						z++;
					}
					if (min(left, right) > currMin)
					{
						currMin = min(left, right);
						currMax = max(left, right);
						currPosition = k;
					}
					else if (min(left, right) == currMin)
					{
						if (max(left, right) > currMax)
						{
							currMin = min(left, right);
							currMax = max(left, right);
							currPosition = k;
						}
						else if (max(left, right) == currMax)
						{
							if (currPosition < k)
								continue;
							else if (currPosition == 0)
								currPosition = k;
						}
					}
				}
				
			}
			Array[currPosition] = 1;
			counter++;
			minimal = currMin;
			maximal = currMax;
			currMin = 0, currMax = 0;
			currPosition = 0;
		}
			x = max(minimal, maximal);
			y = min(minimal, maximal);
		fout << "Case #" << i << ": " << x << ' ' << y << endl;
		i++;
		counter = 1;
	}

	return 0;
}