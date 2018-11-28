#include <iostream>  
#include <cstdio>
using namespace std; 

int main(void){
	int t,k; 
	cin >> t; 
	string s; 
	for(int c =1;c<=t;c++){
		cin >> s >> k;
		int count=0;
		int len = s.length(),flag =0; 
		for(int i=0;i < len; i++){ 
			flag = 0;
			if(s[i]=='-'){
				if(len - i < k) {
					flag =1 ;
					break;
				}
				for(int l=i; l < i+k;l++){
					s[l]= s[l]=='+'?'-':'+';
				}
				count++;
			}
		}
		if(flag ==1 )cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << c << ": " << count << endl;
	}
	return 0;
	
}