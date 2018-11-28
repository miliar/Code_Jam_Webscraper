#include <fstream>
#include <string>
#include <math.h>
using namespace std;

long long getViolation(long long in_number, long long tick){
	long long prev = 0;
	while (tick > 0){
		long long k = in_number / tick;
		if (k < prev){
			return tick;
		}
		else{
			in_number -= tick * k;
			tick /= 10;
			prev = k;
		}
	}
	return tick;
}

long long getNumber(long long in_number){
	long long prev = 0;
	long long n = (long long)floor(log(in_number) / log(10));
	long long mt = 1;
	long long prev_violation = 0;
	for (long long i = 0; i < n; ++i){
		mt *= 10;
	}
	long long cur_violation = 0;
	while ((cur_violation = getViolation(in_number, mt)) > prev_violation){
		long long k = (in_number % (cur_violation * 10)) / cur_violation;
		in_number -= (k + 1) * cur_violation;
		prev_violation = cur_violation;
	}
	if (cur_violation == 0){
		return in_number;
	}
	else{
		return (in_number / prev_violation + 1) * prev_violation - 1;
	}
	
}

int main(int argc, char** args){
	ifstream in_file("input.txt");
	ofstream out_file("output.txt");

	int T;
	in_file >> T;
	long long number;
	for (int t = 0; t < T; ++t){
		in_file >> number;
		long long rst = getNumber(number);

		out_file << "Case #" << t + 1 << ": "<<rst<<std::endl;
	}

	return 0;
}