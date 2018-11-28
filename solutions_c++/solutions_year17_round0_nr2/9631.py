#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

bool check(string num){
	for(int i=0; i<num.length()-1; i++){
		if(num[i] > num[i+1])return false;
	}
	return true;
}

int main(int argc, char** argv) {
	ifstream in("input.txt");
	ofstream out("output.txt");
	
	long long n;
	in >> n;
	
	for(int h=0; h<n; h++){
		
		long long num;
		in >> num;
		
		
		for(long long i=num; i>=0; i--){
			long long x = i;
			ostringstream convert;
			convert << x;
			bool res = check(convert.str());
			if(res){
				out <<"Case #" << h+1 << ": " << i << endl;
				break;
			}
		}	
	}	
	
	
	return 0;
}
