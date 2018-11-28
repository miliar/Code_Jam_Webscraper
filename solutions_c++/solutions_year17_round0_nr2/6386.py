#include<iostream>
#include <vector>
#include <string>
#include <fstream>    /* ifstream / ofstream */
#include <algorithm>  /* std::min */
 
std::vector<std::string> tokenize(const std::string& str, const std::string& delimiters = " ") {
	std::vector<std::string> retVal;
	std::string::size_type startPos = str.find_first_not_of(delimiters, 0);
	std::string::size_type endPos = str.find_first_of(delimiters, startPos);
	while (std::string::npos != startPos || std::string::npos != endPos) {
		retVal.push_back(str.substr(startPos, endPos - startPos));
		startPos = str.find_first_not_of(delimiters, endPos);
		endPos = str.find_first_of(delimiters, startPos);
	}
	return retVal;
}
std::vector<size_t> tokenize_ints(const std::string& str, const std::string& delimiters = " ") {
	std::vector<size_t> retVal;
	std::string::size_type startPos = str.find_first_not_of(delimiters, 0);
	std::string::size_type endPos = str.find_first_of(delimiters, startPos);
	while (std::string::npos != startPos || std::string::npos != endPos) {
	  retVal.push_back(std::stoi(str.substr(startPos, endPos - startPos)));
	  startPos = str.find_first_not_of(delimiters, endPos);
	  endPos = str.find_first_of(delimiters, startPos);
	}
	return retVal;
}
bool has_suffix(const std::string &str, const std::string &suffix) {
	return str.size() >= suffix.size() && str.compare(str.size() - suffix.size(), suffix.size(), suffix) == 0;
}
bool has_prefix(const std::string &str, const std::string &prefix) {
	return str.size() >= prefix.size() && str.compare(0, prefix.size(), prefix) == 0;
}
std::string replace_all(std::string str, const std::string& from, const std::string& to) {
	size_t startPos = 0;
	while ((startPos = str.find(from, startPos)) != std::string::npos) {
		str.replace(startPos, from.length(), to);
		startPos += to.length();
	}
	return str;
}
 
int main(int argc, char* argv[]) {
	std::vector<std::string> args(argv, argv + argc);
	args.erase(args.begin());
	if (args.size() >= 2) {
		std::ifstream input(args.at(0));
		if (input) {
			std::string line;
			std::vector<std::string> lines;
			std::ofstream output(args.at(1));
			while (std::getline(input, line)) {
				lines.push_back(line);
			}
			if (lines.size() > 0) {
				size_t totalTestcases = std::stoi(lines.at(0));
				totalTestcases = std::min(totalTestcases, (lines.size() - 1));
				for (size_t i = 0; i < totalTestcases; i++) {
					/* TODO: write your code here :-) */
					int n = 0, m = 0, pos_last_increase;
					std::string str = lines.at(i+1);
					if(str.size() == 1){
						output << "Case #" << (i+1) << ": " << str << std::endl;
						continue;
					}
					pos_last_increase = -1;
					for( n = 0; n < str.size() - 1; n++){
						m = str[n] - str[n+1];
						if( m < 0 ){
							pos_last_increase = -1;
							continue;
						} else if( m == 0){
							if( pos_last_increase == -1 ){
								pos_last_increase = n;
							}
					//		std::cout << "n " << n << std::endl << "pos " << pos_last_increase << std::endl;
							continue;
						} else {
							if( pos_last_increase == -1 ){
								pos_last_increase = n;
							}
							break;
						}
					}
					if( n == str.size() - 1 ){
						pos_last_increase = -1;
					}
					//std::cout << "case #" << (i+1) << ": " << pos_last_increase << std::endl;
					//std::cout << "case #" << (i+1) << ": " << str[n] + std::string("") << std::endl;
					if( pos_last_increase == -1 ){
						output << "Case #" << (i+1) << ": " << str << std::endl;
						continue;
					} else if ( pos_last_increase == 0 ){
						if( n == str.size() - 1 ) {
							output << "Case #" << (i+1) << ": " << str << std::endl;
							continue;
						}
					}
					output << "Case #" << (i + 1) << ": " << str.substr(0, pos_last_increase);
					if( pos_last_increase != 0 || str[0] != '1' ){
						output << std::stoi( str[n] + std::string(""))  - 1;
					}
					//output << "Case #" << (i + 1) << ": " << str.substr(0, n-1) << std::stoi( std::string(str[n],1) ) - 1;
					for(m = 0; m < str.size() - pos_last_increase - 1 ; m++) { output << '9';}
					output << std::endl;
				}
			}
		}
	}
	return EXIT_SUCCESS;
}
