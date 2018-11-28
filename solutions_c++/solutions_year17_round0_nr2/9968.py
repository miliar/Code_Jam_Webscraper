#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int isTidy(string str) {
	int max = '0';
	for(int i = 0; i < str.length(); i++) {
		if(str[i] < max) return 0;
		max = str[i];
	}
	return 1;
}

int main() {
	ifstream f;
	f.open("test.in");
	ofstream o;
	o.open("out.txt");

	string line;
	int c = 1;
	while(getline(f, line)) {
		int k = 1;
		while(!isTidy(line)) {
			line[line.length()-k] = '9';
			line[line.length()-k-1]--;
			k++;
		}
		while(line[0] == '0') line = line.substr(1,line.length()-1);
		o << "Case #" << c << ": " << line << endl;
		c++;
	}
	f.close();
}
