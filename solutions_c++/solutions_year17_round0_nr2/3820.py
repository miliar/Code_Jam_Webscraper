#include <algorithm>
#include <iostream>
#include <istream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <streambuf>
#include <string>
#include <vector>

using namespace std;

// Problem is to create the last seen tidy number till now.
// A number is tidy if all its digits are non-decreasing when read
// from left to right
int main(){
	
	int i, j, t, T, K;
	string S;

	cin>>T;
	for(t=1; t<=T; t++){
		cin>>S;

		int n = S.length();
		vector<int> a;
		// Step 1. Separate the digits and store in an integer array
		for(i=n-1; i>=0; i--){
			a.insert(a.begin(), (S.at(i) - '0'));
		}

		// Step 2. Track from end to start if the digits are non-increasing
		for(i=n-1; i>0; i--){
			if(a[i-1]>a[i]){
				a[i-1]--;
				a[i] = 9;
				for(j=i; j<n; j++){
					a[j] = 9;
				}
			}
		}

		// Print output
		cout<<"Case #"<<t<<": ";
		i = 0;
		while(a[i]==0) i++;
		for(; i<n; i++){
			cout<<a[i];
		}
		cout<<endl;
		
	}
	
	return 0;
}