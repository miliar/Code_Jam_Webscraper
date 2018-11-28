#include <iostream>
#include <fstream>
#include <cstring>

//#define SIZE 20

using namespace std;


void tidyfy (string & numbers){
	int length;
	length = numbers.length();
	
	bool flag_untidy = false;
	
	for (int i = 0; i < length ; i++){
		// untidy check is only needed for the N-1 cases.
		
		if(flag_untidy == true) {
			//numbers.replace(i, 1, "9");
			numbers[i] = '9';
		}
		else if ( i < length - 1){ // if tidy and not in the last round, check tidy
			if ( numbers[i] > numbers[i+1]){
				flag_untidy = true;
//  				cout << "untidy " << i <<endl;
				
				int flip_pos = 0; // if not found, must be 0;
				// starting backwards and find the position that need to flip
				for (int j = i; j > 0; j-- ){ // not considering [0]
					
					if (numbers[j] > numbers[j-1]) { // found the position
// 						cout << "found at " << j << endl;
						
						flip_pos = j;
						break;
					}
				}
				
				// found the flip pos, -1 
				numbers[flip_pos] = numbers[flip_pos] - 1;
				
				// set the following to be 9
				for (int j = flip_pos + 1; j <= i ; j++){
					numbers[j] = '9';
				}
			}
		}
	}

}

int main(int argc, char **argv) {
	
	ofstream fout ("output.txt");
	ifstream fin ("B-large.in");
	
	int n; // number of text cases
	//char numbers[SIZE]; // > 1000
	string numbers;
	int k; // temp var for flip pan size
	int result;
	
// 	for (int i =0 ; i < SIZE; i++){
// 		numbers[i] = '\0';
// 	}
	
	
	if( fin.is_open() ){
		fin >> n;
		for(int i =0 ; i < n ; i++) {
			fin >>  numbers;
			//cout << numbers << endl;
			int l = numbers.length();

			//START ALGORITHM
			tidyfy( numbers );
			
// 			cout << "Case #" << (i+1) << ": " << numbers << endl;
			
			if (numbers[0] == '0') {
				fout << "Case #" << (i+1) << ": " << numbers.substr(1,l) << endl;
			}
			else {
				fout << "Case #" << (i+1) << ": " << numbers << endl;
			}

		}
	}
	
    return 0;
}

