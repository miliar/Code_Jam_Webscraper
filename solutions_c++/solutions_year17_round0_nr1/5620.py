#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ofstream output ("output.txt");
	ifstream inputfile ("input.in");
	int cases = 0;
	inputfile >> cases;
	for (int cas = 0; cas < cases; cas++){
		string input;
		int K;
		inputfile >> input;
		inputfile >> K;
		int answer = 0;
		for (int i = 0; i < input.length() + 1 - K; i++){
			if (input[i] == '-'){
				answer++;
				for (int j = i; j < i + K; j++){
					if (input[j] == '-'){
						input[j] = '+';
					}
					else{
						input[j] = '-';
					}
				}
				i = 0;
			}
		}
		bool possible = true;
		for (int i = 0; i < input.length(); i++){
			if (input[i] == '-'){
				possible = false;
				break;
			}
		}
		if (possible){
			output << "Case #" << cas + 1 << ": " << answer << endl;
		}
		else{
			output << "Case #" << cas + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}

