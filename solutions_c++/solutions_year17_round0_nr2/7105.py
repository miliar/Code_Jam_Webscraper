#include <iostream>
using namespace std;

int main(){
	int n;
	string s;
	while(cin >> n){
		
		for(int i=0; i<n; i++){
			
			cin >> s;
			
			for(int j=s.size()-1;j>0;j--)
				
				if(s[j] < s[j-1]){
					s[j-1]--;
					for(int k=j;k<s.size();k++)
						s[k] = '9';
				}
			
			for(int j=0;j<s.size()-1;j++)
				if(s[j]=='0')
					s.erase(0,1);
				else
					break;
				
			cout << "Case #" << i+1 << ": " << s << endl;
		}
	}	
	return 0;
}
			
