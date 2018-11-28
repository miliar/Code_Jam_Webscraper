#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
int main(){
	int n,k,cont;
	string s;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> s;
		cin >> k;
		cont=0;
			for(int j=0;j <= s.size()-k;j++){
				if(s[j] == '-'){
					for(int a=0;a<k;a++){
						if(s[j+a]=='-'){
							s[j+a]='+';
						}
						else{
							s[j+a]='-';						
						} 
									
					}
					cont++;	
				}						
			}
		bool flag = true;
		for(int j=0;j<s.size();j++){
			//cout << s[j];
			if(s[j]=='-'){
				flag=false;
				break;			
			}
		}	


	cout << "Case #"<< i+1 <<": ";
	if(flag) cout << cont << endl;
	else cout << "IMPOSSIBLE" << endl;

	}
	

return 0;
}	
