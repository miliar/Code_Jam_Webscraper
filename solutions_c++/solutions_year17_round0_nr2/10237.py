#include <iostream>
#include <string>
#include <cmath>
#include <fstream>

using namespace std;


int main(int argc, char *argv[]) {
	
	ifstream in;
	ofstream out;
	string fname;
	cout << "Input File: ";
	cin >> fname;
	in.open(fname.c_str());
	out.open("B.txt");
	
	int T, N;
	in >> T;
	
	for(int i = 1; i <= T; i++){
		in >> N;
		int tidy = 1;
		for(int n = N; n >= 1; n--){
			string num = to_string(n);
			bool a = true;
			for(int j = 0; j<num.length()-1; j++)
				if(num[j] > num[j+1]){a = false; break;}
			
			if(a){
				tidy = n;
				break;
			}
		}
		
		out << "Case #" << i << ": " << tidy <<endl;
	}
	
}