#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int numOfFlips = 0;
int counter = 1;

// If a '-' exists in the string
string flip(string S, unsigned int K, unsigned int index)
{
	unsigned int size = index + K;

	while(index < size){
		if(S[index] == '-'){
			S[index] = '+';
		}else{
			S[index] = '-';
		}	
		index++;
	}
	return S;
}

// Master Method
bool masterFlip(string S, unsigned int K)
{	
	for(unsigned int i = 0; i <= S.length() - K; i++){
		if(S[i] == '-'){
			S = flip(S, K, i);
			numOfFlips++;	
		}
	}	

	unsigned int index = S.length() - K;
	while(index < S.length()){
		if(S[index] == '-'){
			return false;
		}
		index++;
	}
	return true;
}

// Write to outputfile
void output(bool B)
{	
	string oString;

	if(B){
		oString = "Case #" + to_string(counter) + ": " + to_string(numOfFlips);
		cout << oString << '\n';
	}else{
		oString = "Case #" + to_string(counter) + ": IMPOSSIBLE";
		cout << oString << '\n';
	}
	numOfFlips = 0;
}

int main(int argc, char* argv[]) 
{	
	// Gets T value
	int T;
	cin >> T;

	string S;
	unsigned int K;
	while(counter <= T){
		
		cin >> S;
	
		// finding our pan size
		cin >> K;
		
		// Print correct output
		output(masterFlip(S,K));

		// iterator
		counter++;
	}
	counter--;
	
	return 0;	
}
