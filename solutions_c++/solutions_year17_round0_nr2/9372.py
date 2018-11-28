#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
bool checkNonDecreasing(int n){
	int previousDigit = n%10;
	while(n!=0){		
		n /=10;
		int digitNow = n%10;
		if(previousDigit<digitNow){return false;}
		previousDigit = digitNow;

	}
	return true;
}
int checkTheSeries(int n){
	bool NonDecrease = checkNonDecreasing(n);
	while(!NonDecrease){
		NonDecrease = checkNonDecreasing(n);
		if(NonDecrease){break;}
		--n;
	}
	return n;

}

int main (){
	//opening input file
	ifstream input;
	string line;
	input.open("C:\\Users\\tim12\\Desktop\\B-small-attempt0.txt");
	vector<int> numbers;
	int number;
	while(input >> number){numbers.push_back(number);}

	/*
	int size = numbers.size();
	for (int i = 0; i < size; ++i)
	{
		cout<< numbers[i]<<endl;
	}
	*/

	ofstream fout;
	fout.open("C:\\Users\\tim12\\Desktop\\output2.txt");

	int T = numbers[0];
	for(int i=0; i<T; i++){
		fout << "Case #"<<i+1<<": "<< checkTheSeries(numbers[i+1])<<endl;
	}
	fout.close();
}
