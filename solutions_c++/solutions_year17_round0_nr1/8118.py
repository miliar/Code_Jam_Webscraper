#include <iostream>
#include <fstream>
#include <cstring>

#define CAKE_SIZE 1024

using namespace std;

int calc (char * cakes, int k){
	
	int lenth;
	lenth = strlen (cakes);
	
	int counter = 0;
	
	// scan from left to right
	// for each scan consider [i] to [i+k-1]	
	for (int i = 0; i < lenth - k + 1; i++){
		if (cakes[i] == '+' && (i != lenth - k) ) {
			
			// if not in the last round and no need to flip, skip!
			continue; 
		}
		else if (cakes[i] == '-') {  // if not, judge if need to flip.
			//flip
			for (int j = i; j < i+k ; j++){
				if(cakes[j] == '-'){
					cakes[j] = '+';
				}
				else {
					cakes[j] = '-';
				}
			}
			
			counter ++;
		}
		
		// after flipping, if ending condition meet, end.
		
		if(i == lenth - k ){
			// judge
			
			//cout << "judge" << endl;
			//cout << cakes << endl;
			
			int flag = 0;
			for (int j = i; j < i+k ; j++){
				if( cakes [j] == '-'){
					flag = 1;
				}
			}
			
			if( flag == 0){
				return counter;
			}
			else{
				return -1;
			}
		}
		
		//cout << cakes[i+k-1];
		
	}
	
	
	// if not possible return -1
	return -1;
}

int main(int argc, char **argv) {
	
	ofstream fout ("output.txt");
	ifstream fin ("A-large.in");
	
	int n; // number of text cases
	char cakes[CAKE_SIZE]; // > 1000
	int k; // temp var for flip pan size
	int result;
	
	for (int i =0 ; i < CAKE_SIZE; i++){
		cakes[i] = '\0';
	}
	
	
	if( fin.is_open() ){
		fin >> n;
		for(int i =0 ; i < n ; i++) {
			fin >>  cakes >> k;
			//cout << cakes << endl;
			//cout << k << endl;
		
			//START ALGORITHM
			result = calc(cakes, k);
			if(result >=0 ){
				fout << "Case #" << (i+1) << ": " << result << endl;
			}
			else{
				fout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
			}
			
		}
	}
	
	
    return 0;
}

