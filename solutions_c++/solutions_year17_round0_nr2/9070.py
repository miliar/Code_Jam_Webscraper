//g++ -std=c++14 -Wall -Werror -O2 -o tidy tidy.cpp
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
#include <stdlib.h> 

using namespace std;


int main(){
	ofstream myfile;
	myfile.open ("pan.out");
	int cases;
	cin >> cases;
	// printf("cases = %d\n",cases);
	for(int i = 1; i <= cases; ++i){
		int count = 0;
		long long in;
		string temp;
		cin  >> in;
		// cout << "INPUT = " << in << "\n";


		for(long long j = in; j > 9; j--){
			count = 0;
			temp = to_string(j);
			for(int k = 0; k < temp.size()-1; ++k){
				// cout << "j = " << j << " and string = " << temp << "\n";
				// cout << "first = " << temp[k] << " second = " << temp[k+1] << "\n";
				if((int)temp[k] <= (int)temp[k+1]){
					count++;
				} else {
					break;
				}
			}
			// printf("count = %d\n",count );
			// printf("~~~~~~\n");
			if(count == temp.size()-1){
				myfile << "Case #" << i << ": " << j << "\n";
				break;
			}
		}

		if(in < 10){
			myfile << "Case #" << i << ": " << in << "\n";
		}

	}
	
	myfile.close();
	return 0;
}