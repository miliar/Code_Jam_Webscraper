#include<iostream>
#include<fstream>

#include<vector>

#include<string.h>
#include<math.h>

using namespace std;

unsigned long long int max(unsigned long long int a, unsigned long long int b) {

	if(a > b)
		return a;
	else 
		return b;

}

unsigned long long int min(unsigned long long int a, unsigned long long int b) {

	if(a < b) 
		return a;
	else
		return b;

}

void stalls(unsigned long long int N, unsigned long long int K, unsigned long long int &mini, unsigned long long int &maxi) {

	// We compute the right generation
	unsigned long long int g = floor(log2(K));

	// We computer the position of K in the right generation
	unsigned long long int p = pow(2,g);

	// We check the remaining available stalls
	unsigned long long int r = N - p + 1;

	// We now get the size of the largest available spaces for the right generation
	unsigned long long int s = ceil((double)r/p);

	// Smallest available spaces, now
	unsigned long long int ss = s - 1;

	// We finally check whether the right generation contains one or two classes
	unsigned long long int c = r + p * (1 - s);

	// If K falls in the first class, i.e. one of the largest spaces
	if (K - p + 1 <= c) {

		maxi = floor(s/2);
		if (s % 2 == 0)
			mini = max(maxi - 1, 0);
		else
			mini = maxi;

	}

	// Second class
	else {

		maxi = floor(ss / 2);
		if (ss % 2 == 0)
			mini = max(maxi - 1, 0);
		else
			mini = maxi;

	}

}

int main(int argc, char** argv) {

	ifstream my_file;
	ofstream output(argv[2]);

	my_file.open(argv[1]);
	int T;
	my_file >> T;

	unsigned long long int N, K, mini, maxi;

	int cas = 1;
	int cpt = 0;

	while(cpt < T) {

		mini = 0;
		maxi = 0;

		my_file >> N >> K;

		stalls(N, K, mini, maxi);
		output << "Case #" << cas << ": " << maxi << " " << mini << endl;

		cpt++;
		cas++;

	}

	my_file.close();
	output.close();
	
	return 0;

}
