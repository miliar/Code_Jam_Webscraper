#include <iostream>
using namespace std;

int main(){
	int n,k,r;
	string s;
	bool impossible;
	while(cin >> n){
		for (int i=0; i<n; i++){
			cin >> s >> k;
			r = 0;
			impossible = false;
			for(int j=0;j<s.size()-k+1;j++){
				if(s[j]=='-'){
					r++;
					s[j] = '+';
					for(int l=1;l<k;l++){
						s[j+l] = (s[j+l]=='-' ? '+' : '-');
					}				
				}
			}
			for(int j=s.size()-k+1;j<s.size();j++)
				if(s[j]=='-'){
					impossible = true;
					break;
				}
				
			
			cout << "Case #" << i+1 << ": ";
			(impossible ? cout << "IMPOSSIBLE" : cout << r) ;
			cout << endl;
		}
	}	
	return 0;
}
			
