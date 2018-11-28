//g++ -std=c++14 -Wall -Werror -O2 -o pancake pancake.cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <math.h>
#include <stack>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <fstream>

using namespace std;


int main(){
	ofstream myfile;
	myfile.open ("pan.out");

	int cases;
	int flip;
	int tot = 0;
	string input;
	cin >> cases;
	for(int i = 1; i <= cases; ++i){
		tot = 0;
		cin >> input >> flip;
		for(int j = 0; j < input.size()-flip+1; ++j){
			if(input[j] == '-'){
				tot++;
				for(int z = j; z < j+flip; ++z){
					if(input[z] == '-'){
						input[z] = '+';
					} else {
						input[z] = '-';
					}
				}
			}
		}
		int j;
		for(j = 0; j < input.size(); ++j){
			if(input[j] == '-'){
				break;
			} 
		}
		if(j == input.size()){
			myfile << "Case #" << i << ": " << tot << "\n";
		} else {
			myfile << "Case #" << i << ": IMPOSSIBLE\n";
		}		
	}
	
	myfile.close();
	return 0;
}