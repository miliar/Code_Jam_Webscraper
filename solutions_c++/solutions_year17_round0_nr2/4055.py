#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main(int argc, char* argv[])
{
	argv[1] = "D:\\Other\\BISHI\\GoogleCodeJam\\B\\ex.in";
	argv[2] = "D:\\Other\\BISHI\\GoogleCodeJam\\B\\ex.out";

	//ifstream fin(stdin);
	//ofstream fout(stdout);
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	string line;
	getline(fin, line);
	int testNum = stoi(line);
	for (int i = 0; i < testNum; i++)
	{
		getline(fin, line);
		for (int j = 1; j<line.length(); j++)
		{
			if (line[j - 1]>line[j])
			{
				for (int m = j; m < line.length(); m++)
					line[m] = '9';
				line[j - 1] = '0' + (line[j - 1] - '0' - 1);
				while (j - 1 != 0 && line[j - 1] < line[j - 2])
				{
					line[j - 1] = '9';
					line[j - 2] = '0' + (line[j - 2] - '0' - 1);
					j--;
				}
				break;
			}
		}
		
		int head = 0;
		while (line[head] == '0')head++;
		fout << "Case #" << i + 1 << ": " << line.substr(head, line.length()-head) << endl;
	}

	fin.close();
	fout.close();
}