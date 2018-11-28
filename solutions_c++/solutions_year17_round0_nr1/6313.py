#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	ifstream infile ("A-large.in");
	infile >> T;
	for (int t = 0; t < T; ++t)
	{
		string N_str;
		infile >> N_str;
		bool array[N_str.length()];
		int i = 0;
		for(char &c : N_str){
			if (c == '-')
				array[i] = false;
			else
				array[i] = true;
			i++;
		}
		int K;
		infile >> K;
		int len = N_str.length();
		int count = 0;
		for (int i = 0; i <= len - K; ++i)
		{
			if (!array[i])
			{
				for (int j = 0; j < K; ++j)
				{
					array[i + j] = !array[i + j];
				}
				count++;
			}
		}
		bool flag = false;
		for (int i = 0; i < len; ++i)
		{
			if (!array[i])
			{
				flag = true;
				cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
				break;
			}
		}
		if (!flag)
		{
			cout << "Case #" << (t+1) << ": " << count << endl;
		}
	}
	infile.close();
	return 0;
}