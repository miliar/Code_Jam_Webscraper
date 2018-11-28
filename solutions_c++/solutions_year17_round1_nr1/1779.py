
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;


int main(){
	int T;
	cin >> T;

	for(int tsc=0; tsc<T; tsc++){
		int R,C;
		cin >> R >> C;
		vector<vector<char> > cake(R,vector<char>(C,'?'));
		vector<vector<char> > filler(R,vector<char>(C,'?'));

		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				cin >> cake[i][j];
				filler[i][j] = cake[i][j];
			}
		}

		for(int i=0; i<R; i++){
			int j=0;
			while(j < C && cake[i][j] == '?') j++;
			if(j == C) continue;
			char t = cake[i][j];
			while(j >= 0) filler[i][j] = t, cake[i][j] = t, j--;
		}

//		for(int i=0; i<R; i++){
//			for(int j=0; j<C; j++){
//				cout << filler[i][j];
//			}
//			cout << endl;
//		}

		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if(cake[i][j] != '?') continue;

				int k=j;
				int l = i;
				bool done = false;
				while(l < R){
					k = j;
					while(k >= 0){
						if(cake[l][k] == '?'){
							k--;
							continue;
						}
						filler[i][j] = cake[l][k];
						done = true;
						break;
					}
					if(done) break;
					l++;
				}
			}
		}

//		for(int i=0; i<R; i++){
//			for(int j=0; j<C; j++){
//				cout << filler[i][j];
//			}
//			cout << endl;
//		}

		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if(filler[i][j] != '?') continue;

				int l = i;
//				cout << "i="<<i<<" j="<<j<<endl;
				while(l >= 0){
					if(filler[l][j] != '?') break;
					l--;
				}
				filler[i][j] = filler[l][j];
			}
		}

		cout << "Case #"<<tsc+1<<":" << endl;
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				cout << filler[i][j];
			}
			cout << endl;
		}
	}
}
