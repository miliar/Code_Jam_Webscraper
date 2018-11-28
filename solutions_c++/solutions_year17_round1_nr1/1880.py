#include <iostream>
#include <cstdio>

using namespace std;

char cake[30][30];

int f(int x, int y, int r, int c){
	for(int i=x+1 ; i < r && cake[i][y] =='?' ; i++){
		cake[i][y] = cake[x][y];
	}
	for(int i=x-1 ; i >= 0 && cake[i][y] =='?' ; i--){
		cake[i][y] = cake[x][y];
	}
}

int f2(int x, int y, int r, int c){
	//cout << "Entre en f2 con x y : " << x << y << endl;
	for(int i=y+1 ; i < c && cake[x][i] =='?' ; i++){
		cake[x][i] = cake[x][y];
	}
	for(int i=y-1 ; i >= 0 && cake[x][i] =='?' ; i--){
		cake[x][i] = cake[x][y];
	}
}


int main(){
	int t,p;
	cin >> t ;
	p = t;
	while (t--){
		//Your code here
		int r,c;
		bool a=false;
		cin >> r >> c;
		
		for (int i=0 ; i< r ; i++){
			for (int j=0 ; j< c ; j++){
				cin >> cake[i][j];
			}
		}
		// f1
		for (int i=0 ; i< r ; i++){
			for (int j=0 ; j< c ; j++){
				if(cake[i][j] != '?'){
					f(i,j,r,c);
				}
			}
		}
		//ara revisar si hay ?
		for (int i=0 ; i< r && !a ; i++){
			for (int j=0 ; j< c && !a; j++){
				if(cake[i][j] == '?'){
					a = true;
				}
			}
		}
		//Para f2
		if (a){
			//cout << "entre en for para f2" << endl;
			for (int i=0 ; i< r ; i++){
				for (int j=0 ; j< c ; j++){
					if(cake[i][j] != '?'){
						f2(i,j,r,c);
					}
				}
			}
		}
		
		cout <<"Case #" << p-t << ": "<< endl;
		for (int i=0 ; i< r ; i++){
			for (int j=0 ; j< c ; j++){
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
}
