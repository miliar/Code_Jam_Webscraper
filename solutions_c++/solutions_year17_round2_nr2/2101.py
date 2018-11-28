#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int te=1; te<=t; te++){
		int n,r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v; 
		int a[n];
		if(r > 0){
			a[0] = 1;
			r--;
		}
		else if(y > 0){
			a[0] = 3;
			y--;
		}
		else{
			a[0] = 2;
			b--;
		}
		int fl = 1;
		for(int i=1; i<=n-2; i++){
			if(a[i-1] == 1){
				if(b > 0 && y > 0){
					if(b > y){
						a[i] = 2;
						b--;
					}
					else{
						a[i] = 3;
						y--;
					}
				}
				else if(b > 0){
					a[i] = 2;
					b--; 
				}
				else if(y > 0){
					a[i] = 3;
					y--;
				}
				else{
					fl = 0;
					break;
				}
			}
			if(a[i-1] == 2){
				if(r > 0 && y > 0){
					if(r > y){
						a[i] = 1;
						r--;
					}
					else{
						a[i] = 3;
						y--;
					}
				}
				else if(r > 0){
					a[i] = 1;
					r--; 
				}
				else if(y > 0){
					a[i] = 3;
					y--;
				}
				else{
					fl = 0;
					break;
				}
			}
			if(a[i-1] == 3){
				if(b > 0 && r > 0){
					if(b > r){
						a[i] = 2;
						b--;
					}
					else{
						a[i] = 1;
						r--;
					}
				}
				else if(r > 0){
					a[i] = 1;
					r--; 
				}
				else if(b > 0){
					a[i] = 2;
					b--;
				}
				else{
					fl = 0;
					break;
				}
			}
		}
		if(fl == 0){
			cout << "Case #" << te << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		else{
			int f1 = 0, f2 = 0, f3 = 0;
			if(a[n-2] == 1 || a[0] == 1)
				f1 = 1;
			if(a[n-2] == 2 || a[0] == 2)
				f2 = 1;
			if(a[n-2] == 3 || a[0] == 3)
				f3 = 1;
			if(f1 == 0 && r > 0){
				a[n-1] = 1; 
			}
			else if(f2 == 0 && b > 0){
				a[n-1] = 2;
			}
			else if(f3 == 0 && y > 0){
				a[n-1] = 3;
			}
			else{
				fl = 0;
			}
		}
		if(fl == 0){
			cout << "Case #" << te << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		else{
			cout << "Case #" << te << ": ";
			for(int i=0; i<n; i++){
				if(a[i] == 1)
					cout << "R";
				if(a[i] == 2)
					cout << "B";
				if(a[i] == 3)
					cout << "Y";
			}
			cout << endl;
		}
		//r = 1, b = 2, y = 3
	}
	return 0;
}
