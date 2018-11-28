#include <iostream>
#include <iomanip>    
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream output;
	ifstream input;
	input.open("a_large.txt");
	output.open("a_large_output.txt");
	
	int tc;
	input >> tc;
	for (int ti = 1; ti <= tc; ti++) {
		double maxt = 0;
		int d, k;

		

		input >> d >> k;
		for (int i = 0; i < k; i++) {
			int ki, si;
			input >> ki >> si;
			double ti = (d - ki) / (double) si;
			maxt = maxt < ti ? ti : maxt;

		}
		output << fixed << setprecision(30) << "Case #" << ti << ": " << d / maxt << endl;
	}
	input.close();
}