#include<iostream>
#include<fstream>

#include<string.h>

using namespace std;

bool is_tidy(string S) {

	int n = S.size();
	bool is = true;

	int pos = 0;

	while(pos < n -1) {

		if(S[pos] > S[pos+1])

			return false;

	}

	return true;

}

string last_tidy(string S) {

	int n = S.size() - 1;
	int pos = S.size() - 1;

	while(pos >= 0) {

		if(S[pos] < S[pos-1]) {

			for(int i = n; i >= pos; i--) {

				S[i] = '9';

			}

			S[pos-1]--;

		}

		pos = pos-1;

	}

	if(S[0] == '0')
		return S.substr(1,S.size());
	else 	
		return S;

}

int main(int argc, char** argv) {

	ifstream my_file;
	ofstream output(argv[2]);

	my_file.open(argv[1]);
	int T;
	string N;
	my_file >> T;

	int cas = 1;
	int cpt = 0;

	while(cpt < T) {

		my_file >> N;
		output << "Case #" << cas << ": " << last_tidy(N) << endl;

		cpt++;
		cas++;

	}

	my_file.close();
	output.close();
	
	return 0;

}
