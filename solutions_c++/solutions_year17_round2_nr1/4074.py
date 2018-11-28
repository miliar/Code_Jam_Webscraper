#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
//#include <algorithm>
//#include <queue>
using namespace std;

void main(){
	int T;
	ifstream infile;
	infile.open("A-small-attempt1.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output2A-do12111.txt");
	infile >> T;
	int i = T;
	while (i){
		int D, N;
		infile >> D >> N;
		vector <int> K, S;
		for (int k = 0; k < N; k++){
			int temp, temp2;
			infile >> temp >> temp2;
			K.push_back(temp);
			S.push_back(temp2);
		}
		double speed, t1, t2, tempT, d;
		if (N == 1) speed = (D) / ((double (D)-K[0])/S[0]);
		else {
			if (K[1] > K[0]) { 
				int tempo = K[1];
				K[1] = K[0];
				K[0] = tempo;
				tempo = S[1];
				S[1] = S[0];
				S[0] = tempo;
			}
			for (int k = 0; k < N - 1; k++){
				t1 = (double(D) - K[k]) / S[k];
				t2 = (double(D) - K[k + 1]) / S[k + 1];
				if (t2 > t1) tempT = t2;
				else {
					d = K[k + 1] + (K[k] - K[k + 1]) / (1 - (double(S[k]) / S[k + 1]));
					tempT = ((d - K[k + 1]) / S[k + 1]) + ((D - d) / S[k]);
				}
			}
			speed = D / tempT;
		}
		outfile.setf(std::ios::fixed, std::ios::floatfield);
		outfile << "Case #" << T - i + 1 << ": " << setprecision(6) << speed << endl;
		i--;
	}
	infile.close();
	outfile.close();
	system("pause");
}