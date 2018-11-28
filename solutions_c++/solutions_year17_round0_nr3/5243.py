#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdio>
#include <cmath>

using namespace std;

const int MAXN = 1000 + 10;
const int MAXM = 1000;  
int r, v, ar, br, av, top, ans, tests, test, Time, n, k, data; 
 
int a[MAXN]; 
string s; 
priority_queue<int> q;

bool desc(int i, int j) { return i > j; }

int main(){
    freopen("3.in","r",stdin); 
    freopen("3.out","w",stdout);

    scanf("%d\n", &tests);
    
    for (test = 1; test <= tests; ++test){
    	cin >> n >> k; 
    	q = priority_queue<int> ();
    	q.push(n);
    	int amax = 0, amin = 0; 
    	for (int i = 0; i < k; ++i) {
    		int x = q.top(); 
    		q.pop(); 
    		if (x % 2 == 1) {
    			amax = (x - 1) >> 1; 
    			amin = amax; 
    		} else {
    			amax = x >> 1; 
    			amin = amax - 1; 
    		}
    		q.push(amax); 
    		q.push(amin);
    		// printf("test #%d: %d %d\n", x, amax, amin);   
    	}
		
    	printf("Case #%d: %d %d\n", test, amax, amin);   
    }   
     
    return 0;  
}
