#include <iostream>
#include <fstream>
using namespace std;
long long input;
bool istidy(long long x){
	int now = 10;
	while ( x > 0 ){
		int dig = x % 10;
		if ( dig > now )
			return false;
		now = dig;
		x /= 10;
	}
	return true;
}
long long tidy(){
	while ( input > 1 ){
		if ( istidy(input) ){
			return input;
		}
		else input --;
	}
}
int main(){ 
    ofstream fout("A.out"); 
	int n;
	cin >> n;
	for ( int i = 0 ; i < n ; i ++ ){
		cin >> input;
		fout << "Case #" << i + 1 <<": " << tidy() <<  endl;
		continue;
	}
	
	return 0;
}
