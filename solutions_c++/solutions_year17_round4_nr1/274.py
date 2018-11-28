#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;





void mainfunc(){
	int N, P;
	cin >> N >> P;
	int count[4];
	for(int i = 0; i < P; i++){
		count[i] = 0;
	}
	for(int i = 0; i < N; i ++){
		int G = 0;
		cin >> G;
		count[G%P]++;
	}
	if(P == 2){
		cout << count[0] + (count[1] + 1)/2 << endl;
	}
	else if(P == 3){
		int result = count[0];
		if(count[1] <= count[2]){
			result += count[1] + (count[2] - count[1] + 2)/3;
		}
		else{
			result += count[2] + (count[1] - count[2] + 2)/3;
		}
		cout << result << endl;
	}
	else if(P == 4){
		int result = count[0];
		if(count[1] <= count[3]){
			result += count[1] + (2*count[2] + count[3] - count[1] + 3)/4;
		}
		else{
			result += count[3] + (2*count[2] - count[3] + count[1] + 3)/4;
		}
		cout << result << endl;
	}
}


int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: " , i);
		mainfunc();
	}
}