#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int getLength(int num){
	int c = 0;
	while(num > 0){
		c++;
		num /= 10;
	}
	return c;
}

vector<int> split(int num, int length){
	vector<int> arr;
	for(int i = 0; i < length; i++){ 
		arr.push_back(num % 10);
		num /= 10;
	}
	return arr;
}

bool isOrdered(vector<int> arr){
	for(int i = 0; i < arr.size() - 1; i++){
		if(arr[i] < arr[i+1]){
			return false;
		}
	}
	return true;
}

bool isSorted(int num){
	int length = getLength(num);
	vector<int> arr = split(num, length);
	return isOrdered(arr);
}

int getMinTidy(int num){
	while(!isSorted(num)){
		num--;
	}
	return num;
}

int main(){
	ifstream fin("a.in");
	int tc;
	fin >> tc;
	int num;
	for(int i = 0; i < tc; i++){
		fin >> num;
		cout << "Case #" << i+1 << ": " <<getMinTidy(num) << endl;
	}
}
