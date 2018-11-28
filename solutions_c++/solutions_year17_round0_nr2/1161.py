#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


void process(string& str){
	while (1){
		size_t i=0;
		for (i = 0; i < str.size()-1; ++i){
			if (str[i] > str[i+1]){
				//-- to the front -- no way to be zero there
				str[i]--;
				//filling '9';
                for (size_t j = i+1; j < str.size(); ++j)
					str[j] = '9';
				break;
			}
		}
		if (i == str.size()-1) break;
	}
	if (str[0]=='0'){
		size_t i;
		for (i=0; i < str.size(); ++i )
			if(str[i] != '0') break;
		if (i == str.size()) --i;
		str.erase(0,i);
	}
	return;
}

int main( int argc, char** argv){
	size_t cnt;
	vector<string> number;
	ifstream ip("input.txt");
	ip >> cnt;
	number.resize(cnt);
	for (size_t i = 0; i < cnt; ++i)
		ip >> number[i];
	ip.close();
	for (size_t i = 0; i < cnt; ++i )
		process(number[i]);
	ofstream op("output.txt");
	for (size_t i = 0 ; i<cnt; ++i)
		op << "Case #" << i+1 <<": " << number[i] << endl;
	op.close();
	return 0;
}
