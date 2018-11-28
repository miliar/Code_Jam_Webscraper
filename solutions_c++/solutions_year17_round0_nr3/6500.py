#include<fstream>
#include<iostream>
#include<string>
#include <bitset> 
using namespace std;

int main()
{
	ifstream input;
	int test_cases;
	input.open("input.in");
	input >> test_cases;
	for (int t = 0; t < test_cases; t++)
	{
		ofstream output;
		int N;
		
		int K;
		input >> N >> K;
		bool* stalls = new bool[N + 1];
		stalls[0] = true;
		stalls[N + 1] = true;
		for (int i = 1; i < N + 1; i++)
		{
			stalls[i] = false;
		}
		for (int i = 0; i < K; i++)
		{
			int max_min_Ls_Rs = -1, max_max_Ls_Rs = -1, stall;
			for (int j = 1; j < N + 1; j++)
			{
				if (stalls[j])
					continue;
				int Ls = 0, Rs = 0;
				int k = 1;
				while (j - k >= 0 && !stalls[j - k])
				{
					Ls++;
					k++;
				}
				k = 1;
				while (j + k <= N+2 && !stalls[j + k])
				{
					Rs++;
					k++;
				}
				int min_Ls_Rs;
				int max_Ls_Rs;
				if (Ls > Rs)
					min_Ls_Rs = Rs;
				else
					min_Ls_Rs = Ls;
				max_Ls_Rs = Ls + Rs - min_Ls_Rs;
				if (max_min_Ls_Rs < min_Ls_Rs)
				{
					max_min_Ls_Rs = min_Ls_Rs;
					max_max_Ls_Rs = max_Ls_Rs;
					stall = j;
				}
				else if (max_min_Ls_Rs == min_Ls_Rs) 
				{
					if (max_max_Ls_Rs < max_Ls_Rs)
					{
						max_max_Ls_Rs = max_Ls_Rs;
						max_min_Ls_Rs = min_Ls_Rs;
						stall = j;
					}
				}
			}
			stalls[stall] = true;
			if (i == K - 1)
			{
				output.open("output.txt", ofstream::app);
				output<<"Case #"<<t+1<<": " <<max_max_Ls_Rs << " " << max_min_Ls_Rs << endl;
			}
		}
	}
}