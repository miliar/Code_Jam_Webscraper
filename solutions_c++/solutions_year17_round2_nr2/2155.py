#include<iostream>
using namespace std;
int main (void){
	int testCases;
	cin >> testCases;
	for(int t=0; t < testCases; t++){
		cout << "Case #"<<t+1<<": ";
		int numUnicorns, numDuals, colors[6];
		cin >> numUnicorns;
		for(int i = 0; i< 6; i++){
			cin >> colors[i];
		}
		if(colors[0] > colors[2]+colors[4]|| colors[2] > colors[0]+colors[4] || colors[4] > colors[0]+colors[2]){
			cout << "IMPOSSIBLE";
		}
		else{
			char prev = '\0';
			while(colors[0] > 0){
				if(prev != 'R'){
					cout << 'R';
					colors[0]--;
					prev = 'R';
				}
				if(colors[2]  < colors[4] && colors[4] > 0){
					cout << 'B';
					colors[4]--;
					prev = 'B';
				}
				else if(colors[2] > 0){
					cout << 'Y';
					colors[2]--;
					prev = 'Y';
				}
			}
			while(colors[2] > 0){
				if(prev != 'Y'){
					cout << 'Y';
					colors[2]--;
					prev = 'Y';
				}
				else{
					cout << 'B';
					colors[4]--;
					prev = 'B';
				}
			}
			while(colors[4] > 0){
				if(prev != 'B'){
					cout << 'B';
					colors[4]--;
					prev = 'B';
				}
			}
		}
		cout << "\n";
	}
}