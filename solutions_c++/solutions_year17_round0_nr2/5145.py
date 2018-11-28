#include<iostream>
#include<string>
#include<map>

using namespace std;

bool check_tidy(unsigned int);

int main(void){
	
	map<unsigned int,unsigned int> prev_tidy;
	
	unsigned int max = 0;
	for(unsigned int i = 1; i <= 1000; i++){
		if(check_tidy(i)){max = i;}
		prev_tidy[i] = max;
	}
	
	int total;
	cin >> total;
	
	unsigned int N;
	
	for(int i = 0; i < total; i++){
		cin >> N;
		cout << "Case #" << i+1 << ": " << prev_tidy[N] << endl;
	}
}

bool check_tidy(unsigned int val){
	string max = to_string(val);
	for(int j = 1; j < max.size(); j++){
		if(max[j] < max[j-1]){return false;}
	}
	return true;
}
	