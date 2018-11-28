#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<fstream>
#include<iomanip>

using namespace std;

int main(){

	ifstream input;
	input.open("A-large.in");

	ofstream output;
	output.open("output.txt");

	int t;
	input>>t;

	for(int i=0;i<t;i++){
		long double d, n;
		input >> d >> n;

		long double total = -1;

		for (int j = 0; j < n; j++) {
			long double d2, v2;
			input >> d2 >> v2;

			d2 = d - d2;
			long double t2 = d2 / v2;

			if (total == -1) {
				total = t2;
			}
			else if (t2 > total) {
				total = t2;
			}

		}
		output <<fixed<< "Case #" << i + 1 << ": " << setprecision(6) << d / total << endl;

	}

	input.close();
	output.close();

	return 0;
}