#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	int t;
	ofstream outfile;
	cin >> t;
	outfile.open("AAA.txt");
	for (int i = 0; i < t; i++)
	{
		outfile << "Case #" << i + 1 << ": ";
		long long number;
		cin >> number;
		vector<long long>vec;
		if (number < 10) { outfile << number << endl; }
		else {
			while (true)
			{
				long long value = number;
				long long d = 1;
				long long digit;
				long long cntr = 0;
				while (value != 0)
				{
					digit = value % 10;
					value = value / 10;
					vec.push_back(digit);

				}
				reverse(vec.begin(), vec.end());
				for (long long l = 0; l < vec.size() - 1; l++)
				{
					if (vec[l] <= vec[l + 1]) { cntr++; }



				}


				if (cntr == (vec.size() - 1))
				{

					outfile << number << endl;
					break;
				}
				else
				{

					number = number - d;
				}
				vec.clear();
			}
		}
	}
	outfile.close();

	return 0;
}
