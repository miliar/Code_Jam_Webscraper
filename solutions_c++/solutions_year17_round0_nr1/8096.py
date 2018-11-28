#include <iostream>
#include <fstream>
using namespace std;

int testCases;// <= 100

void flip(string& row, int pos, int range) {
    for(int i = pos; i < pos + range; i++){
        if(row[i] == '+')
            row[i] = '-';
        else
            row[i] = '+';
    }
}

int main() {
	ifstream in ("a.in");
	ofstream out ("a.out");
	
	in>>testCases;
	
	int caseNumber = 0;
	while(caseNumber++<testCases){// Loops the number of test cases
		string row;
		int flipperRange;
		in>>row>>flipperRange;
		int flips = 0;
		for(int i = 0; i < row.length() - flipperRange + 1; i++) {
			//cout<<i<<endl;
			if(row[i] == '-'){
				flip(row, i, flipperRange);
				flips++;
			}
		}
		out<<"Case #"<<caseNumber<<": ";
		if(row.find('-') != -1) {
			out<<"IMPOSSIBLE"<<endl;
		}
		else {
			out<<flips<<endl;
		}
	}
	
}
