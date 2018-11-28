#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;



int main() {

	ifstream in;
	in.open("C-small-2-attempt0.in");

	ofstream out;
	out.open("output.txt");

	int T;
	in >> T;

	for (int i = 0; i < T; i++)
	{
		out << "Case #" << (i + 1) << ": ";
		//cout << "Case #" << (i + 1) << ": ";

		long long int N, K;

		in >> N;
		in >> K;
		
		long long int level = floor(log2(K) + 1);

		long double value = (long double)(N - K) / pow(2, level);

		if (value - (long long int)value >= 0.5)
		{
			//cout << ceil(value) << " " << floor(value) << endl;
			out << ceil(value) << " " << floor(value) << endl;
		}
		else
		{
			//cout << floor(value) << " " << floor(value) << endl;
			out << floor(value) << " " << floor(value) << endl;
		}
	}


	in.close();
	out.close();
	system("PAUSE");

	return 0;

}