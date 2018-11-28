#include <iostream>
#include <string>
#include <array>
#include <unordered_set>
#include <vector>

#include <algorithm>  
using namespace std;


// -1 means it is tidy
int isTidy(string x){
	for(int i = 0; i<x.size()-1;i++){
		if(x[i]<=x[i+1]){
			continue;
		}
		else {
			return i;
		}
	}
	return -1;
}

int main(){
	int n;
	cin >> n;
	vector<string> numbers;
	for(int i = 0; i<n;i++){
		string num;
		cin >> num;
		numbers.push_back(num);
	}	
	for(int i =0;i<n;i++){
		string myNum = numbers[i];
		int index = myNum.size();
		while(isTidy(myNum) != -1){
			index = isTidy(myNum);
			myNum[index] = myNum[index] - 1;
			for(int x = index+1; x<myNum.size();x++){
				myNum[x] = '9';
			}
		}	
		if(myNum[0] == '0'){
			myNum.erase(myNum.begin(),myNum.begin()+1);
		}
		cout << "Case #" << to_string(i+1) << ": ";
		cout << myNum << "\n";
	}
	
	return 0;
}