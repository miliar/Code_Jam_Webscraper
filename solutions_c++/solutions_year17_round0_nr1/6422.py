#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<algorithm>

using namespace std;

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
 
int main(int argc, char* argv[]){
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
				for (size_t samplenumber = 0; samplenumber < totalTestcases; samplenumber++) {
					//output << "Case #" << (i + 1) << ": " << "TODO" << std::endl;
					/* TODO: write your code here :-) */
	int t = samplenumber + 1;
	string str = lines.at(t).substr(0, lines.at(t).find(" "));

	int k = stoi(lines.at(t).substr(lines.at(t).find(" ") + 1 , string::npos));

	int slength = str.size();
	//int in[8] = { 1, 1, 1, 0, 1, 0, 0, 1};
	int in[ slength ];
	int n,i;
	for( i = 0; i < slength; i++){
		if( str.at(i) == '+' ){
			in[i] = 0;
		} else {
			in[i] = 1;
		}
	}
	// - = 1, + = 0
	int step = 0;

	//int j;
	//for(j=0; j < slength; j++){
	//	cout << in[j];
	//}
	//cout << endl;
	if( k % 2 == 0){
		n=0;
		for( i = 0; i < slength; i++){
			n += in[i];
		}
		if( n%2 == 1){
			output << "Case #" << samplenumber + 1 << ": IMPOSSIBLE" << endl;
					//output << "Case #" << (i + 1) << ": " << "TODO" << std::endl;
			continue;
		}
	}
	i=0;
	n=0;
	while( i < slength - k + 1){
		if( in[i] == 0 ){
		} else if(in[i] == 1){
			step ++;
			for(n=0; n < k; n++){
				in[ i + n ] = ( in[ i + n ] + 1 ) % 2;
			}
		} else {
			cout << "error";
			return 1;
		}
		i ++;
	}
	n = 0;
	i = 0;
	for(i=0; i < k; i++){
		n += in[ slength - i - 1 ];
	//	cout << in[ slength - i - 1];
	}
	//cout << endl << endl;
	if( n == 0){
		//cout << "done in " << step << " steps" << endl;
		output << "Case #" << samplenumber + 1<< ": " << step << endl;
	} else {
		output << "Case #" << samplenumber + 1<< ": IMPOSSIBLE" << endl;
	}
				}
			}
		}
	}
	return 0;
}
