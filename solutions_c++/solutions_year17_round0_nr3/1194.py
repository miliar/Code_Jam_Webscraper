#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>


long long int mask_large(const long long int& number){
	long long int result;
	for(long long int mask = 1; mask; mask <<=1){
		if (number&mask) result = mask;
	}
	return result;
}

std::pair<long long int, long long int> process(long long int capacity, long long int occipant){
	long long mask = mask_large(occipant);
	long long newunit = ( capacity - (mask-1) ) / mask;
	long long excessnum = (capacity - (mask-1)) % mask;
	occipant -= (mask-1);
	capacity = newunit;
	if (excessnum >= occipant) capacity++;
	long long int first, second;
	if (capacity % 2 == 1) first = second = capacity/2;
	else {second = capacity/2; first = second-1;}
	return std::pair<long long int, long long int>(first,second);

	/*
	long long int first, second;
	for (long long int mask = ( mask_large(occipant) >> 1 ); mask; mask>>=1){
		//
		if (capacity % 2 == 1) first = second = capacity/2;
		else {second = capacity/2; first = second-1;}
		if (occipant & mask) capacity = first; // min
		else capacity = second; //max
	}
	if (capacity % 2 == 1) first = second = capacity/2;
	else {second = capacity/2; first = second-1;}
	return std::pair<long long int, long long int>(first,second);
	*/
}

int main(){
	size_t T;
	std::vector<long long int> N, K;
	std::ifstream ip("input.txt");
	ip >> T;
	N.resize(T);
	K.resize(T);
	for (size_t i = 0; i < T; ++i)
		ip >> N[i] >> K[i];
	ip.close();
	std::vector<std::pair<long long int, long long int> > result(T);
	for (size_t i = 0; i < T; ++i)
		result[i] = process(N[i], K[i]);
	std::ofstream op("output.txt");
	for (size_t i = 0; i < T; ++i){
		op << "Case #" << i+1 << ": ";
		op << result[i].second << ' ' << result[i].first << std::endl;
	}
	op.close();
	return 0;
}