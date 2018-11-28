#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<fstream>
#include<iomanip>

using namespace std;

int main(){

	ifstream input;
	input.open("B-small-attempt3.in");

	ofstream output;
	output.open("output.txt");

	int t;
	input>>t;

	for(int i=0;i<t;i++){

		int n, r, o, y, g, b, v;

		input >> n >> r >> o >> y >> g >> b >> v;
		string s;

		int *max = &r;
		int *med = &y;
		int *min = &b;
		if ((*med) > (*max)) {
			int *temp = max;
			max = med;
			med = temp;
		}
		if ((*min) > (*max)) {
			int *temp = max;
			max = min;
			min = temp;
		}
		if ((*min) > (*med)) {
			int *temp = med;
			med = min;
			min = temp;
		}

		if ((*max) > (*min) + (*med)) {
			s = "IMPOSSIBLE";
		}
		else {
			int three = (*min) - ((*max)-(*med));
			for (int j = 0; j < three; j++) {
				if (max == &r)s += 'R';
				else if (max == &y)s += 'Y';
				else if (max == &b)s += 'B';

				if (med == &r)s += 'R';
				else if (med == &y)s += 'Y';
				else if (med == &b)s += 'B';

				if (min == &r)s += 'R';
				else if (min == &y)s += 'Y';
				else if (min == &b)s += 'B';

				(*max)--;
				(*med)--;
				(*min)--;
			}

			int left1 = (*med);
			for (int j = 0; j < left1; j++) {
				if (max == &r)s += 'R';
				else if (max == &y)s += 'Y';
				else if (max == &b)s += 'B';

				if (med == &r)s += 'R';
				else if (med == &y)s += 'Y';
				else if (med == &b)s += 'B';

				(*max)--;
				(*med)--;
			}

			int left2 = (*min);
			for (int j = 0; j < left2; j++) {
				if (max == &r)s += 'R';
				else if (max == &y)s += 'Y';
				else if (max == &b)s += 'B';

				if (min == &r)s += 'R';
				else if (min == &y)s += 'Y';
				else if (min == &b)s += 'B';

				(*max)--;
				(*min)--;
			}
		}
		
		output << "Case #" << i + 1 << ": "<< s  << endl;

	}

	input.close();
	output.close();

	return 0;
}