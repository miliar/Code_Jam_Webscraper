#include <iostream>
#include <stdint.h>
#include <string.h>
#include <vector>
using namespace std;

int main(){
	int test_cases;
	cin >> test_cases;
	int case_no = 0;
	while(test_cases--){
		case_no++;
		uint64_t number,temp;
		cin >> number;
		if(number%10==0)
			number-=1;
		temp = number;
		vector<char> num_reverse;
		while(number>0){
			num_reverse.push_back((char)(number%10+48));
			number = number/10; 
		}
		vector<char> num;
		for(int j = num_reverse.size()-1;j>=0;j--){
			num.push_back(num_reverse[j]);
		}
		int i = 0;
		while(num[i]<=num[i+1])
			i++;
		if(i==num.size()-1){
			cout << "Case #"<< case_no << ": " << temp << endl;
		}
		else{
			while(num[i]==num[i-1])
				i--;
			num[i] -= 1;
			i++;
			while(i<num.size()){
				num[i] = '9';
				i++;
			}
			uint64_t result = 0;
			i = 0;
			while(i<num.size()){
				result = result*10 + (num[i]-48);
				i++;
			}
			cout << "Case #"<< case_no << ": " << result << endl;
		}		
	}
	return 0;
}