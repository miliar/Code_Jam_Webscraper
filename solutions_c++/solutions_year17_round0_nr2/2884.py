#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;




string lastTiny(string number){
	int size = number.size();
	int overwriteDigit = size;
	for (int i=size-1; i>=0; i--){
		if (number[i] < number[i-1]){
			number[i-1] -= 1;
			overwriteDigit = i;
		}
	}
	
	for (int i=overwriteDigit; i<size; i++)
		number[i] = '9';
	

	if (number[0] == '0')
		number.erase(number.begin(), number.begin()+1);

	return number;
}





int main(){

	ifstream infile;
	infile.open("B-large.in");

	int numLines;
	infile>>numLines;

	string number;

	vector<string> numberArr;

	for (int i=0; i<numLines; i++){
		infile>>number;
		numberArr.push_back(number);
	}

	infile.close();

	ofstream outfile;
	outfile.open("B-large.out");

	for (int i=0; i<numLines; i++){
		string number = lastTiny(numberArr[i]);
		outfile<<"Case #"<<(i+1)<<": ";
		outfile<<number;
		outfile<<endl;
	}

	outfile.close();


	return 0;
}