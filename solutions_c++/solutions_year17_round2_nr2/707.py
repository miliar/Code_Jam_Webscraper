#include<bits/stdc++.h>
using namespace std;

#define CR 1
#define CB 2
#define CY 3

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int I = 1; I <= T; ++I){
		cout << "Case #" << I  << ": ";
		int n,r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if(y+b < r or r+y < b or b+r < y) cout << "IMPOSSIBLE" << endl;
		else {
			int cur;
            string aux;
			char st;
			if(b >= y and b >= r) {
				cur = CB;
				aux += st = 'B';
				--b;
			}
			else if(y >= b and y >= r) {
				cur = CY;
				aux += st = 'Y';
				--y;
			}
			else if(r >= b and r >= y) {
				cur = CR;
				aux += st = 'R';
				--r;
			}
			else {
				cur = CB;
				aux += st = 'B';
				--b;
			}
			while(b or y or r){
				if(cur == CR){
					if(b > y) {
						aux += 'B';
						cur = CB;
						--b;
					}
					else if(b == y and st == 'B'){
						aux += 'B';
						cur = CB;
						--b;
					}
					else{
						aux += 'Y';
						cur = CY;
						--y;
					}
				}
				else if(cur == CB){
					if(r > y) {
						aux += 'R';
						cur = CR;
						--r;
					}
					else if(r == y and st == 'R'){
						aux += 'R';
						cur = CR;
						--r;
					}
					else{
						aux += 'Y';
						cur = CY;
						--y;
					}
				}
				else if(cur == CY){
					if(b > r) {
						aux += 'B';
						cur = CB;
						--b;
					}
					else if(r == b and st == 'B'){
						aux += 'B';
						cur = CB;
						--b;
					}
					else{
						aux += 'R';
						cur = CR;
						--r;
					}
				}
			}
            if(aux[0] == aux[aux.size()-1] and n != 1){
				cout << "IMPOSSIBLE" << endl;
			}
            else cout << aux << endl;
		}
	}
}
