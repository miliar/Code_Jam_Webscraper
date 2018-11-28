#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>

int main(int argc, char *argv[])
{
	std::string buffer;
	std::getline(std::cin, buffer);
	int case_count = std::stoi(buffer);	
	std::vector<long int> limits;
	std::vector<std::string> not_tidy;

	for(std::string line; std::getline(std::cin, line); ) {
		limits.push_back(std::stol(line));
	}
	for(int i=0; i<100; i++) {
		std::string number = std::to_string(i);
		int prev = 47;
		bool tidy = true;
		for(char &c : number) {
			if((int)c>=prev) {
				prev = c;
			}
			else {
				tidy = false;
				break;
			}
		}
		if(!tidy) {
			not_tidy.push_back(number);
		}
	}


	for(int i=0; i<case_count; i++) {
		std::string last_tidy;
		std::string number;
		for(long int j=limits[i]; j>0; j--) {
			number = std::to_string(j);
			bool tidy = true;
			for(std::string check : not_tidy) {
				if(strstr(number.c_str(),check.c_str())) {
					tidy = false;
					break;
				}
			}
			if(tidy) {
				break;
			}
			//std::cout << number << " not tidy " << std::endl;
		}
		std::cout << "Case #" << i+1 << ": " << number << std::endl;;
	}

	return 0;
}
