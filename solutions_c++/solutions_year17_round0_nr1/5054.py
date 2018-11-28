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
    freopen("1.in","r",stdin); 
    freopen("1.out","w",stdout);

    scanf("%d\n",&tests);
    
    for (test = 1; test <= tests; ++test){
    	cin >> s >> k;
    	int ans = 0; 
		for (int i = 0; i < s.size() - k + 1; ++i) {
			if (s[i] == '-') {
				++ans; 
				for (int j = i; j < i + k; ++j) {
					s[j] = (s[j] == '-') ? '+' : '-';
				}
			}
		}
		bool success = true; 
		for (int i = s.size() - k + 1; i < s.size(); ++i) {
			if (s[i] == '-') {
				success = false;
				break; 
			}
		}           
		if (success) 
    		printf("Case #%d: %d\n", test, ans);   
    	else
    		printf("Case #%d: IMPOSSIBLE\n", test); 
    }   
     
    return 0;  
}
