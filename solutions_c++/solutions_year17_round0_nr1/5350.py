#include <fstream>
#include <iostream>
#include <cassert>
#include <string>
using namespace std;

int main() {
	int num, idx, k, cnt, j;
	bool check;
	string line;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in", ifstream::in);
	fout.open("A-large.out");
    assert( !fin.fail() );
    fin >> num;
	for (int i = 0; i < num; i++){
		fin >> line >> k;
		cnt = 0;
		j = 0;
		check = false;
		while (j < (line.length()-k+1)){
		    if (line[j] == '-'){
		        for (int l = 0; l < k; l++){
		            if (line[j+l] == '-')
		                line[j+l] = '+';
		            else
		                line[j+l] = '-';
		        }
		        cnt++;
		    } else
		        j++;
		}
		for (j = line.length()-k; j < line.length(); j++){
		    if (line[j] == '-')
		        check = true;
		}
		fout << "Case #" << (i+1) << ": ";
		if (check)
		    fout << "IMPOSSIBLE" << endl;
		else
		    fout << cnt << endl;
	}
	fin.close();
	fout.close();
}