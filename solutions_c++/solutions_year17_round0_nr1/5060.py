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

	for(int a = 0;  a < test_cases; a++){
		string inp;
		cin >> inp;
		int k;
		cin >> k;

		int flips = 0;
		for(int x = 0; x < inp.length()-k+1; x++){
			if(inp[x] == '-'){
				flips++;
				for(int y = 0; y < k; y++){
					if(inp[x+y]  == '-')
						inp[x+y] = '+';
					else
						inp[x+y] = '-';
				}
			}
		}
		int possible = 1;
		tr(inp, it){
			if(*it == '-')
				possible = 0;
		}

		if(possible)
			cout << "Case #" << a+1 << ": " << flips << endl;
		else
			cout << "Case #" << a+1 << ": IMPOSSIBLE" << endl;
	}
    return 0;	
}

