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
	is >> input;
	string currentInput = input;
	for (int i = currentInput.size()-2; i >= 0; i--) {
		if (currentInput[i] > currentInput[i + 1]) {
			currentInput[i] = '0' + ((currentInput[i] - '0') - 1);
			for (int j = i + 1; j < currentInput.size(); j++) {
				currentInput[j] = '9';
			}
			etapes.push_back(currentInput);
		}
	}
	int nbFirstZero = 0;
	for (int i = 0; i < currentInput.size(); i++) {
		if (currentInput[i] != '0')
			break;
		nbFirstZero++;
	}
	output = currentInput.substr(nbFirstZero);

}
int main(int argc, char* argv[]){
	is >> nbTest;

	for(int i=0;i<nbTest;i++){
		executeOneInput();
		out << "Case #" << i + 1 << ": " << output << endl;

	}
}
