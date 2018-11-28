#include <iostream> 
#include <cstdio>

using namespace std;



int t, k;
string s;

int main(){
 	cin >> t;
 	for (int i = 1; i <= t; i++) {
 	 	cin >> s >> k;
 		int n = s.size();
 		cout << "Case #" << i << ": ";
 		int bad =0 , res = 0;
 		for (int j = 0; j < n; j++)	
 			if (s[j] == '-') {
 			 	if (j+k > n) {
 			 	 	cout << "IMPOSSIBLE\n";
 			 	 	bad = 1;
 			 	 	break;
 			 	}
 			 	for (int r = j; r < j + k; r++)
 			 		if (s[r] == '-')s[r] = '+'; else s[r] = '-';
 			 	res++;
 				
 			}
 		if (!bad) {
 		 	cout << res << endl;
 		}
 	 
 	}
}