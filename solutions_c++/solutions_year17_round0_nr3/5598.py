#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
const int max = std::numeric_limits<int>::max();
void getTestCases(int& inT, vector<int> & inS, vector<int>&inK) {
	int tc = 0;
	string input = "";
	getline(cin, input);
	stringstream myStream(input);
	myStream >> inT;
	inS.resize(inT);
	inK.resize(inT);

	int tempNum = 0, numBath =0, numPpl=0;
	while (tc < inT) {
		getline(cin, input);
		std::size_t spaceLoc = input.find_last_of(' ');
		stringstream myStream(input.substr(0,spaceLoc));
		myStream >> numBath;
		inS[tc] = numBath;
		stringstream myStream1(input.substr(spaceLoc,input.size()));
		myStream1 >> numPpl;
		inK[tc] = numPpl;
		tc++;
	}
}
void setValue(vector<int>& bathL, vector<int>& bathR) {
	//first fill left value
	int left = 0,right = 0, rightSize = bathR.size(),leftSize = bathL.size(),counter=0;
	while (counter < leftSize) {
		if (bathL[counter] == max) {
			left = 0;
		}else {
			bathL[counter] = left;
			left++;
		}
		counter++;
	}
	//right value set
	counter = rightSize - 1;
	while (counter >= 0) {
		if (bathR[counter] == max) {
			right = 0;
		}
		else {
			bathR[counter] = right;
			right++;
		}
		counter--;
	}
}
int getMin(int a, int b) {
	if (a < b)
		return a;
	 return b;
}
int getMax(int a, int b) {
	if (a < b)
		return b;
	return a;
}
int getBestIndex(vector<int>& bathL, vector<int>&  bathR) {
	vector<int> maxIndexVec ;
	int maxIndex = -1, maxIndexValue = 0, counter =0, maxOfMin =-1;
	vector<int> temp;
	temp.resize(bathL.size());
	while (counter < bathL.size()) {
		if (!(bathL[counter] == max || bathR[counter] == max)) {
			temp[counter] = getMin(bathL[counter], bathR[counter]);
			if (temp[counter] > maxOfMin) {
				maxOfMin = temp[counter];
				maxIndex = counter;
				maxIndexVec.clear();
				maxIndexVec.push_back(counter);
			}
			else if (temp[counter] == maxOfMin) {
				maxIndexVec.push_back(counter);
			}
		}
		counter++;
	}
	//get filter index of who has max value in Ls Rs
	counter = 0;
	int maxOfMax = -1;
	while (counter < maxIndexVec.size()) {
		int temp = getMax(bathL[maxIndexVec[counter]], bathR[maxIndexVec[counter]]);
		if (maxOfMax < temp) {
			maxOfMax = temp;
			maxIndex = maxIndexVec[counter];
		}
		counter++;
	}
	return maxIndex;
}
string getNumberForLastPerson(int bath, int ppl) {
	vector<int> bathL,bathR;
	int totalBath = bath + 2;
	bathL.resize(bath+2);
	bathR.resize(bath+2);
	//first fill value for guard
	bathL[0] = bathR[0] = max;
	bathL[bathL.size() - 1] = bathR[bathR.size() - 1] = max;
	setValue(bathL,bathR);
	int pplCount = 0, index =0, minVal = 0 , maxVal =0;
	while (pplCount < ppl) {
		index = getBestIndex(bathL,bathR);
		if (pplCount + 1 == ppl)
			break;
		bathL[index] = bathR[index] = max;
		setValue(bathL,bathR);
		pplCount++;
	}
	std::string space(" ");
	return (std::to_string(getMax(bathL[index], bathR[index])) + space + std::to_string(getMin(bathL[index], bathR[index])));
}
int main() {
	// your code goes here
	int tc = 0;
	vector<int> S, K;
	vector<string> op;
	getTestCases(tc, S, K);
	int temp = 0;
	op.resize(tc);
	while (temp < tc) {
		op[temp] = getNumberForLastPerson(S[temp],K[temp]);
		temp++;
	}
	temp = 0;
	while (temp < tc) {
		cout << "Case #" << temp+1 << ": "  << op[temp] << endl;
		//cout << "string :" << S[temp] << " flip:" << K[temp] << endl;
		temp++;
	}
	getchar();
	return 0;

}