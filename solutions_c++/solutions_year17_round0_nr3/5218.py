#include <iostream>
#include <string>
#include <array>
#include <unordered_set>
#include <vector>
#include <math.h> 
#include <algorithm>  
#include <queue>
using namespace std;


int main(){
	int n;
	cin >> n;
	vector<unsigned long long> numStallsArray;
	vector<unsigned long long> numPeopleArray;
	for(int i = 0; i<n;i++){
		unsigned long long temp;
		cin >> temp;
		numStallsArray.push_back(temp);
		cin >> temp;
		numPeopleArray.push_back(temp);
	}	
	for(int i =0;i<n;i++){
		priority_queue<unsigned long long> myQ;

		unsigned long long stalls = numStallsArray[i];
		unsigned long long people = numPeopleArray[i];
		// unsigned long long maxNum;
		// unsigned long long minNum;
		if(stalls == people){
			cout << "Case #" << to_string(i+1) << ": ";
			cout << "0 0" << "\n";	
			continue;
		}
		//still look at size differently
		myQ.push(stalls+1);
		unsigned long long maxNum;
		unsigned long long minNum;
		for(unsigned long long x = 0;x<people;x++){
			unsigned long long myNum = myQ.top();
			myQ.pop();
			minNum = myNum/2;
			maxNum = myNum - minNum;
			myQ.push(maxNum);
			myQ.push(minNum);
		}
		// //we will look at size a bit differently
		// stalls++;	

		// //THIS CODE MIGHT NOT WORK, RISKY DOUBLE -> INT conversion
		// double numBigSplitsD = log2(people);
		// unsigned long long numBigSplits = (int) numBigSplitsD;
		// unsigned long long remainingOperations = people - numBigSplits;

		// for(int i = 0; i<numBigSplits; i++){

		// }	
		cout << "Case #" << to_string(i+1) << ": ";
		cout << maxNum - 1 << " " << minNum - 1 << "\n";
		// //MAKE SURE TO DO -1 AT THE END
	}
	
	return 0;
}