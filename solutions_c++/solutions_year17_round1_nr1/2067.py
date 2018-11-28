#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int main(){
	
	int n;
	
	int r,c;
	cin >> n;
	for(int k=0;k<n;k++){
		char m[26][26];
		cin >> r >> c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){	
				char x;
				cin >> x;
				m[i][j] = x;				
			}		
		}
		char atual;
		for(int i=0;i<r;i++){
			atual= '?';
			for(int j=0;j<c;j++){	
				if(m[i][j] != '?') {
					//cout << i <<j << endl;
					atual = m[i][j];
					for(int q=0;q<j;q++){
						if(m[i][q] == '?')
							m[i][q] = atual;
						
					}
				}
				else if(m[i][j] == '?' && atual !='?'){
					m[i][j] = atual;				
				}
							
			}		
		}



		for(int i=0;i<c;i++){
			atual= '?';
			for(int j=0;j<r;j++){
				//cout << j << i <<" "<< m[j][i] << " " << atual<< endl;
				if(m[j][i] != '?') {
					atual = m[j][i];
					//cout << "aki" << endl;					
					for(int q=0;q<j;q++){
						//cout <<q << j << " " << m[q][j] <<  endl;
						if(m[q][i] == '?')
							m[q][i] = atual;
						
					}
				}
				else if(m[j][i] == '?' && atual !='?'){
					//cout << j << i << atual << endl;
					m[j][i] = atual;				
				}
							
			}		
		}
		cout << "Case #"<< k+1 <<": " << endl;

		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){	
				
				cout << m[i][j];				
			}		
		cout << endl;
		}
		
	}
	return 0;
}	
