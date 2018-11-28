#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int min_time(string pan, int len);

int main(){

	int tcase;
	string pan;
	int len;
	int mintime;

	cin >> tcase;

	for (int i=1; i<=tcase; ++i){
		cin >> pan >> len;
		mintime = min_time(pan,len);
		if(mintime <0) { cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;}
		else {cout << "Case #" << i << ": " << mintime << endl; }
	}

}


int min_time(string pan, int len ){
	int total = pan.length();
	char* panc = new char[pan.length() + 1];
	strcpy(panc, pan.c_str());

	int flip = 0;
	for (int i=0; i<total; i++){
		if (pan[i] == '-'){
			if (( total -i) < len) { delete [] panc; return -1;}
			int j=1;
			// flip pancake after it 
			while (j<len){
				if (pan[i+j] == '+') { pan[i+j] = '-';}
				else {pan[i+j] = '+';}
				j++;
			}
		flip++;
		}else {continue;}
	}
	delete [] panc;
	return flip;
}
