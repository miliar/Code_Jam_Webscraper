#include <iostream>
using namespace std;

int main() {
	int testcase;
	cin >> testcase;
	string state;
	int k,i;
	int flipCount;
	bool impossible;
	for(int t=1;t<=testcase;t++){
	    flipCount = 0;
	    cin >> state >> k;
	    cout << "Case #" << t<<": ";
	    for(i=0;i+k<=state.size();i++){
	        if(state[i] == '-'){
	            //flip
	            for(int j=0;j<k;j++)
	                state[i+j] = (state[i+j] == '-' ? '+':'-');
	            flipCount++;
	        }
	    }
	    impossible = false;
	    for(;i<state.size();i++)
	        if(state[i] == '-')
	            impossible = true;
	    if(!impossible)
	        cout << flipCount << endl;
	    else
	        cout << "IMPOSSIBLE" << endl;
	    
	}
	return 0;
}