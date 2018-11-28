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
	vector<string> pancakesArray;
	vector<int> flipSizeArray;
	for(int i = 0; i<n;i++){
		string temp;
		cin >> temp;
		int num;
		cin >> num;
		pancakesArray.push_back(temp);
		flipSizeArray.push_back(num);
	}	

	for(int i = 0;i<n;i++){
		int flipsize = flipSizeArray[i];
		string pancakes = pancakesArray[i];
		int totalFlips = 0;	
		int x = 0;
		for(x = 0;x<=pancakes.size() - flipsize;x++){
			if(pancakes[x] == '-'){
				totalFlips++;
				//flip it
				for(int y=0;y<flipsize;y++){
					if(pancakes[x+y] == '-'){
						pancakes[x+y] = '+';
					}
					else {
						pancakes[x+y] = '-';
					}
				}
			}
		}
		for(;x<pancakes.size(); x++){
			if(pancakes[x]=='-'){
				totalFlips = -1;
				break;
			}
		}
		cout << "Case #" << to_string(i+1) << ": ";
		if(totalFlips == -1){
			cout << "IMPOSSIBLE";
		}
		else {
			cout << to_string(totalFlips);
		}
		cout << "\n";
	}
	return 0;
}

// flipsize = 3
// size = 5
// 01234
// +++-+
// i need to flip 2
// size - flipsize = 2