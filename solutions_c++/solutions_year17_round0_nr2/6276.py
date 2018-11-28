#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	ifstream infile ("B-large.in");
	infile >> T;
	for (int t = 0; t < T; ++t)
	{
		string N_str;
		infile >> N_str;
		int array[N_str.length()];
		int i = 0;
		for(char &c : N_str){
			array[i] = c - 48;
			i++;
		}
		int len = N_str.length();
		for (int i = len - 2; i >= 0; i--)
		{
			if (array[i] > array[i+1])
			{
				array[i]--;
				for (int j = i + 1; j < len; ++j)
				{
					array[j] = 9;
				}
			}
		}
		int first = 1;
		cout << "Case #" << (t + 1) << ": ";
		for (int i = 0; i < len; ++i)
		{
			if (first && (array[i] == 0))
				continue;
			else{
				first = 0;
				cout<<array[i];
			}
		}
		cout << endl;
	}
	infile.close();
	return 0;
}