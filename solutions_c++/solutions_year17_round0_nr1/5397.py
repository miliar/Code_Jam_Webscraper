#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
int halt = 0;
void getTestCases(int& inT, vector<string> & inS, vector<int>& inK) {
	int tc = 0;
	string input = "";
	getline(cin, input);
	stringstream myStream(input);
	myStream >> inT;
	inS.resize(inT);
	inK.resize(inT);
	int tempNum = 0;
	while (tc < inT) {
		getline(cin, input);
		std::size_t spaceLoc = input.find_last_of(' ');
		inS[tc] = input.substr(0, spaceLoc);
		stringstream myStream(input.substr(spaceLoc, input.size()));
		myStream >> tempNum;
		inK[tc] = tempNum;
		tc++;
	}
}
void removeBoundary(string& str, int& start, int& end) {
	//first from left
	
	while (start <= end && str[start] == '+' )
		start++;
	while (start <= end && str[end] == '+')
		end--;

}
void forceFullyFlip(string &str, int&start, int&end, int ktr) {
	if (!(end - start + 1 >= ktr)) {
		halt = 1;
		return;
	}
	int temp = 0;
	while (temp < ktr) {
		if (str[start + temp] == '-')
			str[start + temp] = '+';
		else
			str[start + temp] = '-';
		temp++;
	}
}
void setBoundaryFlip(string & str, int ktr, int& start, int &end, int &numFlip) {
	if (start > end)//on equal one element will be left
		return;
	if (start == end && str[start] == '+')
		return;

	int left = start, right = end;
	int leftBound = left + ktr, rightBound = right - ktr;
	bool leftCheck = false, rightCheck = false;

	if (right - left + 1 < ktr) { // if flip size is more then element then return
		halt = 1;
		return;
	}

	//first for left
	while (left < leftBound) {
		if (str[left] == '-')
			leftCheck = true;
		else {
			leftCheck = false;
			break;
		}
		left++;
	}
	if (leftCheck == true) {
		start = start + ktr;
		numFlip++;
	}
	//then for right
	if (start < end && end - start + 1 >ktr) {//if start is less then end and there is still left position for right side flip 
		while (right > rightBound) {
			if (str[right] == '-')
				rightCheck = true;
			else {
				rightCheck = false;
				break;
			}
			right--;
		}
		if (rightCheck == true) {
			end = end - ktr;
			numFlip++;
		}
	}
	if (leftCheck || rightCheck) {
		removeBoundary(str, start, end);
		setBoundaryFlip(str, ktr, start, end, numFlip);
	}
	else {
		if (end - start +1 < ktr)
			halt = 1;
	}
}
int	getNumberOfFlip(string str, int ktr) {
	//cout << "input str :" << str << "number of flip" << ktr << endl;
	int num = 0;
	int start = 0;
	int end = str.size() - 1;

	while (start < end && halt == 0) {
		removeBoundary(str, start, end);
		setBoundaryFlip(str, ktr, start, end, num);
		if (start < end && halt == 0) {
			forceFullyFlip(str, start, end, ktr);
			num++;
		}
	}
	//cout << "output str : " << num << endl;
	return num;
}

int main() {
	// your code goes here
	int tc = 0;
	vector<string> S;
	vector<int> K;
	vector<int> op;
	getTestCases(tc, S, K);
	int temp = 0;
	//cout << "op: num of tc :" << tc << endl;
	op.resize(tc);
	while (temp < tc) {
		op[temp] = getNumberOfFlip(S[temp], K[temp]);
		if (halt == 1)
			op[temp] = std::numeric_limits<int>::max();
		temp++;
		halt = 0;
	}
	temp = 0;
	while (temp < tc) {
		if(op[temp] == std::numeric_limits<int>::max())
			cout << "Case #" << temp + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << temp+1 << ": "  << op[temp] << endl;
		//cout << "string :" << S[temp] << " flip:" << K[temp] << endl;
		temp++;
	}
	getchar();
	return 0;

}