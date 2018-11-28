#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
	long long int T, N, K, occ,i;
	long long int L_s, R_s;
	vector<long long int> vals;
	map<long long int,long long int> occurances;
	ifstream infile("C-large.in");
	ofstream outfile("outlargeC.txt");

	infile >> T;
	for (int t = 0; t < T; t++) { //for every test case
		outfile << "Case #" << t + 1 << ": ";
		infile >> N >> K;
		vals.clear();
		occurances.clear();
		for (i = 0; i < K; i++) {
			if (N == 1) {
				L_s = 0;
				R_s = 0;
				break;
			}
			L_s = N / 2;

			if(N % 2 == 0){//even
				R_s = L_s - 1;
			}
			else {//odd
				R_s = L_s;
			}

			if (find(vals.begin(), vals.end(), L_s) != vals.end()) {}
			else vals.push_back(L_s);
			if (find(vals.begin(), vals.end(), R_s) != vals.end()) {}
			else vals.push_back(R_s);

			/*
			cout << "vec----------------------------------------------->";
			for (int k = 0; k < vals.size(); k++) {
				cout << vals[k] << " ";
			}
			cout << endl;
			*/

			occ = occurances[N];
			if (occ > 1) {
				occurances[L_s] += occ;
				occurances[R_s] += occ;
				i = i + occ - 1;
				
				vector<long long int>::iterator ptr = max_element(vals.begin(), vals.end());
				N = *ptr;
				vals.erase(ptr);
				continue;
			}

			occurances[L_s]++;
			occurances[R_s]++;

			vector<long long int>::iterator ptr = max_element(vals.begin(), vals.end());
			N = *ptr;
			vals.erase(ptr);

			//printf("iteration:%d, N:%d,occ:%d, L:%d, R:%d \n", i, N,occ, L_s, R_s);
		}
		//cout << "**********" << endl;
		outfile << L_s << " " << R_s << "\n";
	}
	return 0;
}
