#include <iostream>

using namespace std;

#define Aman Jain

int main(){
	int testcase, kflip, length, flag, counter, i, j;
	string pancakes;
	cin >> testcase;
	for(int k=0;k<testcase;k++){
		flag = 0;
		counter = 0;
		cin >> pancakes >> kflip;
		length = pancakes.length();
		for(i=0;i<=length-kflip;i++){
			if(pancakes[i]=='-'){
				counter++;
				for(j=0;j<kflip;j++){
					if(pancakes[i+j]=='-')
						pancakes[i+j]='+';
					else
						pancakes[i+j]='-';
				}
			}
		}
		for(;i<length;i++){
			if(pancakes[i]=='-'){
				flag = 1;
				break;
			}
		}
		if(flag)
			cout << "CASE #" << k+1 << ": IMPOSSIBLE" << endl;
		else
			cout << "CASE #" << k+1 << ": " << counter << endl;
	}
	return 0;
}