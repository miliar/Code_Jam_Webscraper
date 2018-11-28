#include <iostream>
#include <fstream>
#include <cstring>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <stack>
#include <list>	
#include <algorithm>
#include <limits.h>

using namespace std;

ifstream f("pbB.in");
ofstream g("pbB.out");

bool isTidy(int x){
	int prevDigit = x % 10;
	x = x/10;

	if(x == 0){
		return true;
	}

	while(x != 0){
		int digit = x % 10;
		x = x / 10;
		if (prevDigit < digit){
			return false;
		}
		prevDigit = digit;
	}
	return true;
}

int main(){
	int t;
	f >> t;

	for(int i = 1; i <= t; i++){
		int inter;
		f >> inter;
		for(int j = inter; j >= 0; j--){
			if (isTidy(j)){
				g << "Case #" << i << ": " << j << endl;
				break;
			}
		}
	}

	return 0;
}