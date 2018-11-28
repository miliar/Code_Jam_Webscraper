#include<fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		string x;
		fin >> x;
		bool needsWork = true;
		while (needsWork)
		{
			int max = '0';
			bool didWork = false;
			for (int i = 0; i < x.length(); i++) {
				if (x[i] >= max) {
					max = x[i];
				}
				else {
					didWork = true;
					x[i - 1]--;
					for (int j = i; j < x.length(); j++)
						x[j] = '9';
				}
					
			}
			needsWork = didWork;
		}//true

		int leading = 0;
		for (char c : x) {
			if (c == '0')
				leading++;
			else
				break;
		}
		x.erase(0, leading);
		fout << "Case #" << t + 1 << ": " << x << endl;
	}
}