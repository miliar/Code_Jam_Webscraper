#include<iostream>
#include<math.h>
#include<vector>

using namespace std;

int main(){
	int T;
	cin >> T;
	int R;
	int C;
	for(int i = 0; i<T; i++){
		cin >> R;
		cin >> C;
		char ingrid[25][25];
		char outgrid[25][25];
		for(int it1 = 0; it1 < 25; it1++){
			for(int it2 = 0; it2 < 25; it2++){
				ingrid[it1][it2] = '\0';
				outgrid[it1][it2]= '\0';
			}
		}
		for(int it1 = 0; it1 < R; it1++){
			for(int it2 = 0; it2 < C; it2++){
				cin >> ingrid[it1][it2];
				
				outgrid[it1][it2]=ingrid[it1][it2];
			}
		}
		for(int it1 = 0; it1 < R; it1++){
			for(int it2 = 0; it2 < C; it2++){
				if (ingrid[it1][it2] != '?' && ingrid[it1][it2] != '\0'){
						int temp1 = it2+1;
						int temp2 = it2-1;
						while (outgrid[it1][temp1]=='?'){
							outgrid[it1][temp1] = ingrid[it1][it2];
							temp1++;
						}
						while (outgrid[it1][temp2]=='?'){
							outgrid[it1][temp2] = ingrid[it1][it2];
							--temp2;
						}
				}
			}
		}
		bool state=false;
		while(state==false){
		state=true;
		for(int it1 = 0; it1 < R; it1++){
			for(int it2 = 0; it2 < C; it2++){
				if (outgrid[it1][it2] == '?' || outgrid[it1][it2]=='\0'){
				state=false;
				outgrid[it1][it2] = outgrid[it1+1][it2]=='?'||outgrid[it1+1][it2]=='\0' ? outgrid[it1-1][it2] : outgrid[it1+1][it2];
				}
			}
		}
		}
	
	cout << "Case #" << i+1 << ": " << endl;
	for(int it1 = 0; it1 < R; it1++){
			for(int it2 = 0; it2 < C; it2++){
				cout << outgrid[it1][it2];
			}
			cout << endl;
		}
	}
	return 0;
}