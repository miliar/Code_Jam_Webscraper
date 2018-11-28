#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> numbers;

int mod(int a, int b) {
    int r = a % b;
    return r < 0 ? r + b : r;
}

long vectorToLong (vector<int> & n){
	long cum = 0l;
	for (int i = n.size() -1, p = 0; i >= 0; i--, p++){
		if (n[i] != 0)
			cum += n[i] * (long)pow (10, p);
	}
	
	return cum;
}

void minusOne (vector<int> & number){
	if (number[number.size()-1] > 0){
		number[number.size()-1]--;
		return;
	}
	for (int i = number.size()-1; i>= 0; i--){
		number[i]--;
		if (number[i] < 0){
			if (i == 0){
				number[i] = 0;
			} else{
				number[i] = 9;
				number[i-1]--;
				
				if (number[i-1] >= 0)
					return;
			}
		}
	}
}

bool isTidy(vector<int> & number){
	//cout << "Is " << vectorToLong (number) << " tidy?" << endl;
	if (number.size() == 1)
		return true;
	for (int i = 1; i<number.size(); i++)
		if (number[i-1] > number[i])
			return false;
	
	return true;
}

long getTidy (vector<int> & n){
	while (!isTidy(n))
		minusOne (n);
	
	return vectorToLong (n);
}

int main(){
	int n;
	cin >> n;
	
	numbers.resize(n);
	char c;
	cin.get(c);
	for (int i = 0; i<n; i++){
		 cin.get(c);
		 while (c != '\n'){
		 	numbers[i].push_back ((int)c-48);
		 	cin.get(c);
		 }
	}
	
	for (int i = 0; i<numbers.size(); i++){
		cout << "Case #" << i+1 << ": " << getTidy (numbers[i]) << endl;
	}
		
	return 0;
}
