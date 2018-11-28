#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main(int argc, char** argv) {
	ifstream in("input.txt");
	ofstream out("output.txt");
	
	int n,k;
	string s;
	in >> n;
	for(int h=0; h<n; h++){
		in >> s >> k;
		int sol = 0;
		for(int i=0; i<s.length()-k+1; i++){
			if(s[i] == '-'){
				sol++;
				for(int j=i; j<i+k; j++){
					if(s[j] == '-')s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool si = true;
		for(int i=0; i<s.length(); i++){
			if(s[i] == '-'){
				si = false;
				break;
			}
		}
		if(!si){
			out << "CASE #" << h+1 << ": " <<  "IMPOSSIBLE" << endl;	
		}
		else{
			out << "CASE #" << h+1 << ": " << sol << endl;
		}
	}
	
	
	
	return 0;
}
