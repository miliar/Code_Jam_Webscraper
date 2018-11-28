#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
	int  t = 0;
	cin>>t;
	for(int l = 1; l <= t; l++){
		int r = 0, c = 0;
		cin>>r>>c;
		vector<string> v(r);
		vector<vector<int> > o(r, vector<int>(c,0));
		for(int i = 0; i < r; i++)
			cin>>v[i];
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(v[i][j] != '?'){
					if((j!= 0 && v[i][j-1] == '?') || (j != c-1 && v[i][j+1] == '?')){
						for(int k = j+1; k < c; k++){
							if(v[i][k] != '?') break;
							v[i][k] = v[i][j];
						}	
						for(int k = j-1; k >= 0; k--){
							if(v[i][k] != '?') break;
							v[i][k] = v[i][j];
						}
					}
				}
			}
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(v[i][j] == '?'){
					if(i != 0)
						v[i][j] = v[i-1][j];
					else{
						for(int k = i; k < r; k++){
							if(v[k][j] != '?'){
								v[i][j] = v[k][j];
								break;
							}
						}
					}
				}
			}
		}
		cout<<"Case #"<<l<<":"<<endl;
		for(int i = 0; i < r; i++){
			cout<<v[i]<<endl;
		}
	}
	return 0;
}