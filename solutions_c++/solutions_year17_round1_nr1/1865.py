#include <iostream>
#include <string>
#include <array>
#include <unordered_set>
#include <vector>

#include <algorithm>  
using namespace std;



int main(){
	int n;
	cin >> n;
	vector<vector<string> > cakes;
	vector<int> rows;
	vector<int> cols;
	for(int i = 0; i<n;i++){
		int r, c;
		cin >> r >> c;
		rows.push_back(r);
		cols.push_back(c);
		vector<string> myCake;
		for(int a = 0; a<r;a++){
			string temp;
			cin >> temp;
			myCake.push_back(temp);
		}
		cakes.push_back(myCake);
	}	

	for(int i = 0;i<n;i++){
		vector<string> cake = cakes[i];
		int r = rows[i];
		int c = cols[i];
		int index_of_last_nonblank_row = 100;
		bool isFirstFilledRow = true;
		for(int x = 0; x<r;x++){
			int indexOfLastInitial = -1;	
			for(int y = 0;y<c;y++){
				char element = cake[x][y];
				if(element == '?'){
					if(indexOfLastInitial == -1){
						continue;
					}
					else {
						cake[x][y] = cake[x][indexOfLastInitial];
					}
				}
				else {
					if(indexOfLastInitial == -1){
						for(int a = 0;a<y;a++){
							cake[x][a] = cake[x][y];
						}
					}
					indexOfLastInitial = y;
				}
			}

			if(indexOfLastInitial == -1){
				if(x > index_of_last_nonblank_row){
					cake[x] = cake[index_of_last_nonblank_row];
				}
			}	
			else {
				if(isFirstFilledRow){
					for(int a = 0; a<x;a++){
						cake[a]=cake[x];
					}
				}
				isFirstFilledRow = false;
				index_of_last_nonblank_row = x;
			}
		}



		cout << "Case #" << to_string(i+1) << ": \n";
		for(int x = 0;x<r;x++){
			for(int y = 0 ;y<c;y++){
				cout << cake[x][y];
			}
			cout << "\n";
		}
	}
	return 0;
}

// flipsize = 3
// size = 5
// 01234
// +++-+
// i need to flip 2
// size - flipsize = 	2