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

ifstream f("pbA.in");
ofstream g("pbA.out");

int nOFlips(string pancakes, int k){
	int flips = 0;
	for(int i = 0; i <= pancakes.size() - k; i++){
		if(pancakes[i] == '-'){
			//cout << pancakes << endl;
			//cout << " arriveeed at " << i << endl;
			flips++;
			for(int j = i; j <= i + k - 1; j++){
				if(pancakes[j] == '-'){
					pancakes[j] = '+';
				} else {
					pancakes[j] = '-';
				}
			}
		}
	}
	for(int i = pancakes.size() - k + 1; i < pancakes.size(); i++){
		if(pancakes[i] == '-'){
			return -1;
		}
	}
	return flips;

}


int main(){
	int t;
	f >> t;

	for(int i = 1; i <= t; i++){
		string pancakes;
		int k;
		f >> pancakes >> k;

		int res = nOFlips(pancakes,k);
		//cout << res<< endl;
		g << "Case #" << i << ": ";
		if(res != -1){
			g << res << endl;
		} else {
			g << "IMPOSSIBLE" << endl;
		}

	}

	return 0;
}