#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
using namespace std;

const int MAXN = 1000 + 10;
const int MAXM = 1000;  
int r, v, ar, br, av, top, ans, tests, test, Time, n, k, data; 
 
int a[MAXN]; 
string s; 

bool desc(int i, int j) { return i > j; }

int main(){
    freopen("2.in","r",stdin); 
    freopen("2.out","w",stdout);

    scanf("%d\n", &tests);
    
    for (test = 1; test <= tests; ++test){
    	cin >> s;
    	int ans = 0; 
		
		// 2 2 3 1 
		// 2 2 2 9
		
		// 1 2 3 4 5 6 7 8 0
		// 1 2 3 4 5 6 7 7 9
		
		// 1 3 2
		// 1 2 9
		
		// 111111111111111110
		//  99999999999999999
		int n = s.size(); 
		for (int i = 0; i < n - 1; ++i) {
			if (s[i] > s[i + 1]) {
				int j = i; 
				do {
					s[j] = char((int)s[j] - 1); 
					--j;
				} while (j >= 0 && s[j] > s[j + 1]);
				
				++j;
				if (s[j] == '0' && j == 0) {
					s = string(n - 1, '9');
				} else {
					s = s.substr(0, j + 1) + string(n - j - 1, '9');
				}
				break; 
			}
		}
		
    	printf("Case #%d: %s\n", test, s.c_str());   
    }   
     
    return 0;  
}
