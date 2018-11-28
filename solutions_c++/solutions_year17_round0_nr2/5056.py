#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h> 

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

using namespace std;

int main(){
	int test_cases;
	cin >> test_cases;

	for(int a = 0; a < test_cases; a++){
		string N;
		cin >> N;

		for(int x = N.length()-1; x > 0; x--){
			int right_digit = N[x] - '0';
			int left_digit = N[x-1] - '0';

			if(left_digit > right_digit){
				for(int y = x; y < N.length(); y++){
					N[y] = '9';
				}
				N[x-1] = left_digit-1+'0';
			}	
			
		}

		int start = 0;
		if(N[0] == '0' && N.length() > 1)
			start = 1;

		cout << "Case #" << a+1 << ": ";
		for(int z = start; z < N.length(); z++){
			cout << N[z];
		}
		cout << endl;
	}
    return 0;	
}

