#include <fstream>
#include <algorithm>
#include <vector>
#include <string> 
#include <queue>


using namespace std;

int input;
vector<string> etapes;
string output;
ifstream is("test.in");
ofstream error("error.txt");
ofstream out("out.out");
int nbTest;


void executeOneInput(){
	int K;
	is >> input >> K;
	std::priority_queue<int> pq;
	pq.push(input);
	for (int i = 0; i < K-1; i++) {
		char buffer[33];
		int sizeInterval = pq.top();
		pq.pop();
		if (sizeInterval % 2 == 0) { //pair
			pq.push((sizeInterval-1) / 2);
			pq.push((sizeInterval-1) / 2 + 1);
		}
		else {
			pq.push((sizeInterval-1) / 2);
			pq.push((sizeInterval-1) / 2);
		}
		etapes.push_back(_itoa(pq.top(), buffer, 10));
	}
	int sizeInterval = pq.top();
	if (sizeInterval % 2 == 0) { //pair
		char buffer[33];
		output = _itoa((sizeInterval - 1) / 2 + 1, buffer, 10);
		output += " ";
		output += _itoa((sizeInterval - 1) / 2, buffer, 10);
	}
	else {
		char buffer[33];
		output = _itoa((sizeInterval - 1) / 2, buffer, 10);
		output += " ";
		output += _itoa((sizeInterval - 1) / 2, buffer, 10);
	}

}
int main(int argc, char* argv[]){
	is >> nbTest;

	for(int i=0;i<nbTest;i++){
		executeOneInput();
		out << "Case #" << i + 1 << ": " << output << endl;

	}
}
