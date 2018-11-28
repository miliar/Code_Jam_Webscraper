#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <cmath>

#define MAXSIZE 10

template<typename I, typename N>
//I is random-access iterator, N is UnsigedInteger
 I int_to_string(I first, N n){
	I p = first;
	while(n != N(0)){
		*p++ = n % 10 + '0';
		n /=10;
	}
	std::reverse(first,p);
	return p;
}

template<typename N>
N tidy_number(N n){
	char obi[MAXSIZE];
	while(n != N(0)){
		std::string chase(obi, int_to_string(obi,n));
		if(std::is_sorted(chase.begin(),chase.end()))
			return n;
		--n;
	}
	//if it gets here, The whole world perish!
	return 0;
	
}

int main(){
	long chase;
	int count = 1;
	std::ifstream in{"B-small-attempt0.in"};
	std::ofstream out{"result_small.txt"};
	in >> chase;
	while(in>>chase){
		out << "Case #" << count <<": "<<tidy_number(chase)<<std::endl;
		++count;
	}
}