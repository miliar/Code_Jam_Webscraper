#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>      // std::setprecision

using namespace std;


int main(){

	int T;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> T;

	for(int t = 0; t < T ; t++){
		
		long D, N;
		fin >> D >> N;

		vector<float> spds(N);

		double min ; //= 1000000000000.0;
		for(int i = 0; i < N; i++){


			long K, S;
			fin >> K >> S;
			spds[i] = (D*S*1.0)/(1.0*(D-K));
			if(i == 0) min = spds[0];
			if(spds[i] < min) min = spds[i];
		}

	//	vector<float>::iterator spdmin = min_element(spds.begin(), spds.end()); 

		fout << "Case #" << t+1 << ": ";
		fout << setprecision(15) << min <<endl;
	}

	fin.close();
	fout.close();

	return 0;
}
