#include <vector> 
#include <iostream> 
using namespace std;

int flip(vector<int> &arr, int offset, int flip){
	if(offset+flip-1 >= arr.size()) return 0;	
	for(int i=0; i<flip; i++){
		arr[i+offset] = (arr[i+offset]+1)%2;
	}
	return 1;
}
int main() {
    int tests, flipper=0;
	string pancakes="";
    cin >> tests;  
    
    for (int i=1; i<=tests; ++i){
		string line;
  		getline(cin, line);
        cin >> pancakes >> flipper;
		int flips=0; int flag=1;
		vector<int> p;
		for(int j=0; j<pancakes.length(); j++){
			if(pancakes[j]=='-') p.push_back(0);
			else p.push_back(1);
		}
		for(int j=0; j<p.size(); j++){
			if(p[j]==1) continue;
		 	else{
				if( flip(p, j, flipper) == 0 ){ flag=0; break;}
				else flips++;
				
			}	
		}
		
		if(flag==0) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else 		cout << "Case #" << i << ": " << flips << endl;
    }
    return 0;   
}
