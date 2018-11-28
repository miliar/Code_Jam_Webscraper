#include<iostream>
#include<string.h>

#include<fstream>
#include<vector>

using namespace std;

void flip(string& S, int K, int pos) {

	for(int i = pos; i < pos+K; i++) {
	
		if(S[i] == '+')
			S[i] = '-';
		else
			S[i] = '+';	

	}

}

int nb_flips(string S, int K, int flips, int pos) {

	int n = S.size();

	while(S[pos] == '+') {

		pos++;

	}

	if(pos > n - K) {

		for(int i = pos; i < n; i++) {
	
			if(S[i] == '-')
	
				return -1;

		}

		return flips;

	}

	else {

		flip(S, K, pos);
		return nb_flips(S, K, flips+1, pos+1);

	}

} 

int main(int argc, char** argv) {

	ifstream my_file;
	ofstream output("output_A_large");

	my_file.open(argv[1]);
	int T;
	my_file >> T;

	int cas = 1;
	int cpt = 0;

	while(cpt < T) {

		string pancakes;
		int K, res;

		my_file >> pancakes >> K;
		int r = nb_flips(pancakes, K, 0, 0); 	
		
		output << "Case #" << cas << ": ";
		if(r >= 0)
			output << r << endl;
		else
			output << "IMPOSSIBLE" << endl;

		cpt++;
		cas++;

	}

	my_file.close();
	output.close();
	
	return 0;

}	
