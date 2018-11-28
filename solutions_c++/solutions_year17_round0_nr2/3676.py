#include<iostream>
#include<string>
using namespace std;
int main() {
    int T;
    int ans;
    cin >> T;
    for (int t = 0 ; t < T; ++t) {
	string in;
	cin >> in;
	for (int i = 0 ; i+1 < in.size(); ++i) {
	    if (in[i] <= in[i+1]) continue;
	    for (int j = i+1; j< in.size(); ++j) {
		in[j]='9';
	    } 
	    in[i]--;
	    for (int j = i; j>=0; --j) {
		if (in[j-1]<=in[j]) break;
		//  in[j-1]> in[j]
		in[j]='9';
		in[j-1]--;
	    }
	    break;
	}
	cout << "Case #" << (t+1) << ": ";
	for (int i = 0 ; i < in.size(); ++i) {
	    if (in[i]=='0') continue;
	    for (int j = i; j < in.size(); ++j) {
		cout << in[j];
	    } 
	    break;
	}
	cout << endl;
    }

    return 0;
}
