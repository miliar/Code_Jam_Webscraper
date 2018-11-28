#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
using namespace std;



int main(){

	int T;
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	fin >> T;

	for(int t = 0; t < T ; t++){
		
		string s;
		fin >> s;
		int n = s.length();

		for(int j = 0; j < 20; j++){
	
			for(int i = 0; i < n-1; i++){
				if(s[i] > s[i+1]){ 
					s[i]--;
					for(int j = i+1; j< n; j++)
						s[j] = '9';  
				}
			//	cout << s <<endl;
			}
		}


	//	long N = atol(s.c_str());
		s.erase(0, s.find_first_not_of('0'));

		fout << "Case #" << t+1 << ": " << s <<endl;
	}

	fin.close();
	fout.close();

	return 0;
}
