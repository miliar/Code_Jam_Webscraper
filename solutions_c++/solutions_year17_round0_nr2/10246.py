#include <iostream>
#include <sstream>

bool isTidy(unsigned long long n) {
	std::stringstream buffer;
	buffer << n;
	std::string number = buffer.str();
	for(int i = 0; i < number.length() - 1; i++) {
		if(number[i] > number[i+1]) {
			return false;
		}
	}
	return true;
}

int main(){

	unsigned long long t, i = 1, n, last;
	std::cin>>t;
	while(t--){
		last = 0;
		std::cin>>n;
		for(int j = 0; j <= n; j++) {
			if(isTidy(j)) {
				last = j;
			}
		}
		std::cout<<"Case #"<<i++<<": "<<last<<"\n";
	}

	return 0;
}
