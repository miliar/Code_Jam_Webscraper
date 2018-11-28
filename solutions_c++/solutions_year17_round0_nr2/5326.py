#include <fstream>
#include <iostream>
#include <cassert>
#include <string>
using namespace std;

int main() {
	int num;
	string line;
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in", ifstream::in);
	fout.open("B-large.out");
    assert( !fin.fail() );
    fin >> num;
	for (int i = 0; i < num; i++){
		fin >> line;
		for (int j = line.length()-1; j > 0; j--){
		    if (line[j] < line[j-1]){
		        line[j-1]--;
		        for (int k = j; k < line.length(); k++){
		            line[k] = '9';
		        }
		    }
		}
		if (line[0] == '0')
		    line = line.substr(1,line.length()-1);
		fout << "Case #" << (i+1) << ": ";
		fout << line << endl;
	}
	fin.close();
	fout.close();
}