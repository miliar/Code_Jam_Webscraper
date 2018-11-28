#include <fstream>
#include <algorithm>
#include <vector>
#include <string> 


using namespace std;

string input;
vector<string> etapes;
string output;
ifstream is("test.in");
ofstream error("error.txt");
ofstream out("out.out");
int nbTest;

void executeOneInput(){
	int nbFlip;
	is >> input >> nbFlip;
	int nbFlipDone = 0;
	string currentInput = input;
	if (currentInput.size() < nbFlip) {
		output = "IMPOSSIBLE";
	}
	else {
		for (int i = 0; i <= currentInput.size() - nbFlip; i++) {
			if (currentInput[i] == '-') {
				for (int j = i; j < i + nbFlip; j++) {
					currentInput[j] = currentInput[j] == '-' ? '+' : '-';
				}
				etapes.push_back(currentInput);
				nbFlipDone++;
			}
		}
		bool bIsFinished = false;
		for (int i = currentInput.size() - nbFlip; i < currentInput.size(); i++) {
			if (currentInput[i] == '-') {
				output = "IMPOSSIBLE";
				bIsFinished = true;
				break;
			}
		}
		char buffer[33];
		if (!bIsFinished)
			output = _itoa(nbFlipDone, buffer, 10);

	}

}
int main(int argc, char* argv[]){
	is >> nbTest;

	for(int i=0;i<nbTest;i++){
		executeOneInput();
		out << "Case #" << i + 1 << ": " << output << endl;

	}
}
