#include <iostream>
#include <string>

using namespace std;

string get_last_tidy(string N){
	int i = N.length() - 1;
	
	//backward pass
	for(i = N.length() - 1; i > 0; i--) {
		if(N[i] < N[i - 1]) {
			//cout << N[i] << " " << N[i - 1] << endl;
			N[i] = '9';
			if(N[i-1] == '0') {
				N[i-1] = '9';
			} else {
				N[i-1] = N[i-1] - 1 ;
		    }
		    
		    // changing the current digit breaks the sorted order
		    if(i < N.length() - 1 && N[i] > N[i + 1]) {
		    	for(int j = i+1; j < N.length(); j++)
		    		N[j] = '9';
			}
		}
	}
	
	// remove leading zeros
	int startIdx = 0;
	for(; startIdx < N.length(); startIdx++)
		if(N[startIdx] != '0')
		    break;
	return N.substr(startIdx, N.length() - startIdx);
}

int main(int argc, char ** argv) {
	
	int T;
	string N;
	
	cin >> T;
	
	for(int input_no = 0; input_no < T; input_no++) {
		cin >> N;
		cout << "Case #" << (input_no + 1) << ": " << get_last_tidy(N) << endl;
	}
}
/*
11
132
1000
7
111111111111111110
1088
2188
10909
90909
990
890
190

*/
