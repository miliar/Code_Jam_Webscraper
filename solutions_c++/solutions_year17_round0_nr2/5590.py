using namespace std;
#include <iostream>
#include <string>
#include <fstream>

int main()
{
	ofstream output;
	ifstream input ("input.in");
	output.open("output.txt");
	int cases = 0;
	input >> cases;
	for (int cas = 0; cas < cases; cas++){
		string inputstring;
		input >> inputstring;
		int lastequal = 0;
		bool equal = false;
		int end = 0;
		for (unsigned int i = 1; i < inputstring.length(); i++){
			int oldn = inputstring[i - 1] - '0';
			int newn = inputstring[i] -'0';
			if (newn == oldn && equal == false){
				lastequal = i-1;
				equal = true;
			}
			else if (newn < oldn){
				if (equal){
					end = lastequal;
				}
				else{
					end = i-1;
				}
				inputstring[end]--;
				for (unsigned int j = end + 1; j < inputstring.length(); j++){
					inputstring[j] = '9';
				}
				break;
			}
			else if(newn > oldn){
				equal = false;
			}
		}
		if (inputstring[0] == '0'){
			inputstring.erase(inputstring.begin());
		}
		output << "case #" << cas + 1 << ": " << inputstring << endl;
	}
	return 0;
}

