#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
int main(){
	int n;
	long long int mi,ma;
	string s;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> s;
		mi=0;
		ma=s.size()-1;

		for(long long int j=0;j<s.size()-1;j++){
			if(s[j] < s[j+1] && j<s.size()-2){
				mi=j+1; // mi pra frente = 9			
			}
			
			if(s[j] > s[j+1]){
				ma=j; // ma pra frente = 9
				break;			
			}
			
		}
		//cout << mi << " " << ma << endl;
		
	
		cout << "Case #"<< i+1 <<": ";
//cout << "primeiro" << endl;
			
			if(ma<s.size()-1){	// se existe um ponto decrescente		
				for(long long int t=0;t<mi;t++){
					cout << s[t];
				}
			
				int r= int(s[mi]-'0')-1;
				if(r == 0){
					r=9;
					if(mi==0) mi++;			
				}
			
				 
				cout << r;

				for(long long int t=mi+1;t<s.size();t++){
					cout << 9;		
				}		
			}

			else{
				for(long long int t=0;t<s.size();t++){
					cout << s[t];
				}			
			}
		cout << endl;
		

	
	
	}
	

return 0;
}	
