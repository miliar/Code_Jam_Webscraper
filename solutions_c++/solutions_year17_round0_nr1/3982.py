#include <iostream>
#include <string>
using namespace std;

int main() {
	int k, t;
	string input;
	cin >> t;
	for(int caseCount = 1; caseCount <= t; caseCount++) {
	    cin >> input >> k;
	    int flipCount = 0, imp=0, i;
	    for(i=0;i<=input.size()-k;i++) {
	        if(input[i] == '-') {
	            for(int j = i; j < i+k; j++) {
	                if(input[j] == '+') input[j] = '-';
	                else input[j] = '+';
	            }
	            flipCount++;
	        }
	    }
	    for(; i < input.size(); i++) {
	        if(input[i] == '-') {
	            imp = 1;
	            break;
	        }
	    }
	    if(imp == 1)
	        cout << "Case #" << caseCount << ": IMPOSSIBLE" << endl;
	    else
	        cout << "Case #" << caseCount << ": " << flipCount << endl;
	}
	return 0;
}
