#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

vector<bool> transformString(string str){
	int size = str.size();
	vector<bool> ret;
	for (int i=0; i<size; i++){
		ret.push_back(str[i] == '+');
	}
	return ret;
}

void goFlipper(vector<bool> & series, int i, int k){
	for (int x = i; x < i+k; x++)
		series[x] = !series[x];	
}

bool checkSmile(vector<bool> & series){
	for (bool pancake : series)
		if (!pancake)
			return false;
	
	return true;	
}

int solveForString(string str, int k){
	vector<bool> series = transformString(str);
	int size = series.size();
	int flipCount = 0;
	for (int i = 0; i <= size - k; i++){

		if (!series[i]){
			goFlipper(series, i, k);
			flipCount++;
		}
	}
	if (!checkSmile(series))
		return -1;
	return flipCount;
}


int main(){
	ifstream infile;
	infile.open("A-large.in");

	int numLines;
	infile>>numLines;

	string series;
	int flipper;

	vector<string> panLineArr;
	vector<int> flipperArr;

	for (int i=0; i<numLines; i++){
		infile>>series;
		infile>>flipper;
		panLineArr.push_back(series);
		flipperArr.push_back(flipper);
	}

	infile.close();

	ofstream outfile;
	outfile.open("A-large.out");

	for (int i=0; i<numLines; i++){
		int flip = solveForString(panLineArr[i], flipperArr[i]);
		outfile<<"Case #"<<(i+1)<<": ";
		if (flip >= 0)
			outfile<<flip;
		else 
			outfile<<"IMPOSSIBLE";
		outfile<<endl;
	}

	outfile.close();

	return 0;
}