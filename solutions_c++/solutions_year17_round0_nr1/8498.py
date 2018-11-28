#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
using pancakes_t = std::vector<bool>;

bool c2b(char c){
	if(c == '-') return false;
	if(c == '+') return true;	
	return false;
}
char b2c(bool b){
	if(b) return '+';
	else return '-';
}

void printPancakes(pancakes_t & pancakes){
	for(const auto & elem : pancakes){
		cout << b2c(elem);
	}
	cout << endl;
}

bool isSolved(pancakes_t & pancakes){
	bool output = true;
	for(const auto & elem: pancakes){
		output &= elem;
		if( output == false) break;
	}
	return output;
}
 
bool canBeSolved(pancakes_t & pancakes, int k){
	bool output = false;
//	if(k >(int) (pancakes.size()+1)/2) return false;
	return true;
}

int solve(pancakes_t & pancakes, int k){
	int output = 0;
	//cout << "k:" << k << endl;
	for(int i =0 ; i < (int)pancakes.size(); ){
		//printPancakes(pancakes);
		while( i < (int) pancakes.size() && pancakes[i] == 1) i++;
		if(i == (int) pancakes.size()) break;
		if(i + k > (int) pancakes.size()) return -1;
		for(int j = i; j < (int) pancakes.size() && j < i+k; j++){
			pancakes[j] = pancakes[j] ^ true;
		//	cout << b2c(pancakes[j]) << " ";
		}
		output++;
		//cout << endl;
		
	}		
	return output;
}

int solveProblem(pancakes_t pancakes, int k){
	int output = -1;
	if(isSolved(pancakes)){
		output = 0;
	} else {
		if(!canBeSolved(pancakes, k)){
			return -1;
		} else {
			return solve(pancakes, k);
		}
	}

	return output;
}

int main(){
	int t;
	cin >> t;
	for(int i =1; i <=t; i++){
		string vals;
		cin >> vals;
		int k;
		cin >> k;
		pancakes_t pancakes(vals.length());
		for(int j =0; j < (int)vals.length(); j++){
			pancakes[j] = c2b(vals[j]);
		}
		
		int val = solveProblem(pancakes, k);
		stringstream output;
		if(val == -1){
			output << "IMPOSSIBLE";
		} else {
			output << val;
		}
		cout << "Case #" << i << ": " << output.str() << endl;
	}
	return 0;
}
