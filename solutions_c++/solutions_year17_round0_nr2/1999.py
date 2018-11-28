#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(){
	int t, n;
	string s;
	cin >> t;
	for(int c = 1; c<=t;c++){
		cin >> s;
		int size = s.size();
	
		for(int i = size-1; i>0 ; i--){
			if(s[i] < s[i-1]){
				int k = i, n = 1;
				while(s[k-1] > s[k] && k <= size-1){
					s[k] = '9';
					k++;
//					n++;
				}
//				
//				while(n--){
//					s[k] = '9';
//					k--;
//				}
				s[i-1] -= 1;
			}

		}
			
//			cout << i << ' ' << s <<endl;
		
		
	
		printf("Case #%d: ",c);
		if(s[0]=='0') cout << s.substr(1,size-1) << endl;
		else cout << s <<endl;
	}
	
}
