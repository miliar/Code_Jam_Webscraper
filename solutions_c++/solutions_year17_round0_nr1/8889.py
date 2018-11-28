#include <iostream>
#include <string>
#include <fstream>
#include <utility>



template<typename I, typename N>
//I is iterator, N is unsignedInteger
void string_replace(I first, N n){
	while(n != N(0)){
		*first = (*first == '-') ? '+':'-';
		++first; --n;	
	}
}

template<typename I, typename N>
//I is random-access iterator, N is UnsignedInteger
std::pair<I,N> solution(I first, I last, N n){
	N size = N(last - first);
	N result = N(0);
	N count = N(0); 
	
	while(first != last){
		if(*first == '-'){
			++result;
			if(count + n <= size)
				string_replace(first,n);
			else
				return std::make_pair(first,result);
		}
		++first; ++count;
	}
	return std::make_pair(first,result);
}


int main(){
	std::string chase;
	int count = 1;
	int k;
	std::ifstream in {"A-large.in"};
	std::ofstream out {"result_large.txt"};
	in >> k;
	while( in >> chase >> k){
		std::pair<std::string::reverse_iterator, int> p = solution(chase.rbegin(), chase.rend(), k);
		out<< "Case #"<<count<<": ";
		if(p.first == chase.rend())
			out<<p.second;
		else
			out<<"IMPOSSIBLE";
		out<<std::endl;
		++count;
	}
}