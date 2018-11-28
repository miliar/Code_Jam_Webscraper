#include <iostream>
#include <vector>
#include <string>

using namespace std;

void sol(int a, int b, vector<vector<char>> &v){
	vector<vector<bool>> visited(a, vector<bool>(b));
	for(int i = a - 1; i >= 0; --i){
		for(int j = b - 1; j >= 0; --j){
			if(!visited[i][j] && v[i][j] != '?'){
				visited[i][j] = 1;
				int mark_i1 = i, mark_i2 = i;
				int mark_j1 = j, mark_j2 = j;
				while(mark_i1 > 0){
					if(mark_i1 > 0 && v[mark_i1 - 1][j] == '?'){
						v[mark_i1 - 1][j] = v[i][j];
						visited[mark_i1 - 1][j] = 1;
						mark_i1--;					
					}else break;
					
				}
				while(mark_i2 < a - 1){
					if(mark_i2 < a - 1 && v[mark_i2 + 1][j] == '?'){
						v[mark_i2 + 1][j] = v[i][j];
						visited[mark_i2 + 1][j] = 1;
						mark_i2++;
					}
					else break;
				}

				int x = mark_i1 ;
				int y = mark_i2 ;
				//cout << "i = " << i << "j = " << j << "x = " << x << "y = " <<y << endl;
				int whole = true;
				for(; mark_j1 > 0 ; mark_j1--){
					for(int k = x; k <= y; ++k){
						if(mark_j1 > 0 && v[k][mark_j1 - 1] == '?'){
							continue;
						}else{
							whole = false;
							break;
						}
					}
					if(!whole) break;
					for(int k = x; k <=y; ++k){
						v[k][mark_j1 - 1] = v[i][j];
						visited[k][mark_j1 - 1] = 1;
					}
				}

				whole = true;
				for(; mark_j2 < b - 1; mark_j2++){
					for(int k = x; k <= y; ++k){
						if(mark_j2 < b - 1 && v[k][mark_j2 + 1] == '?'){
							continue;
						}else{
							whole = false;
							break;
						}
					}
					if(!whole) break;
					for(int k = x; k <=y; ++k){
						v[k][mark_j2 + 1] = v[i][j];
						visited[k][mark_j2 + 1] = 1;
					}					
				}
				
			}
		}
	}
}



int main(){
	int t;
	cin >> t;
	
	
	for(int i = 0; i < t; ++i){
		
		int a, b;
		cin >> a >> b;
		vector<vector<char>> tb;
		for(int j  = 0; j < a; ++j){
			vector<char> tmp;
			char c;
			for(int i = 0; i < b; ++i){
				cin >> c;
				tmp.push_back(c);
			}
			tb.push_back(tmp);		
		}

		sol(a,b,tb);
		cout << "Case #" << i+1 << ": "  << endl;
		for(int i = 0; i < a; ++i){
			for(int j = 0; j < b; ++j){
				cout << tb[i][j];
			}
			cout << endl;
		}
	}
}