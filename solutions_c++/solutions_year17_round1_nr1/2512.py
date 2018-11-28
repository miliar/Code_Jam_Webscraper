#include <bits/stdc++.h>
using namespace std;
#define lln long long int

int main(){
	lln n;
	cin >> n;
	for(lln u=0;u<n;u++){
		lln x,y;
		cin >> x >> y;
		char grid[x][y];
		for(lln i=0;i<x;i++){
			for(lln j=0;j<y;j++){
				cin >> grid[i][j];
			}
		}
		for(lln i=0;i<x;i++){
			for(lln j=0;j<y;j++){
				if(grid[i][j]!='?'){
					lln p = i, q = i;
					lln flag1=0,flag2=0;
					p--;
					q++;
					while(p>=0 || q<x){//cout << p << " " << q << " " << flag1 << " " << flag2 << " " << grid[p][j] << " " << grid[q][j] << " upper " << endl;
						if(p>=0 and flag1==0 and grid[p][j]=='?'){//cout << "u1";
							grid[p][j] = grid[p+1][j];
							p--;
						}
						else{
							flag1=1;
							p = INT_MIN;
						}
						if(q<x and flag2==0 and grid[q][j]=='?'){//cout << "u2";
							grid[q][j] = grid[q-1][j];
							q++;
						}
						else{
							flag2=1;
							q = INT_MAX;
						}
					}
				}
			}
		}
		for(lln i=0;i<x;i++){
			for(lln j=0;j<y;j++){
				if(grid[i][j]!='?'){
					lln p = j, q = j;
					lln flag1=0,flag2=0;
					p--;
					q++;
					while(p>=0 || q<y){//cout << p << " " << q << " " << flag1 << " " << flag2 << " " << grid[i][p] << " " << grid[i][q] << " niche " << endl;
						if(p>=0 and flag1==0 and grid[i][p]=='?'){//cout << "n1";
							grid[i][p] = grid[i][p+1];
							p--;
						}
						else{
							flag1=1;
							p = INT_MIN;
						}
						if(q<y and flag2==0 and grid[i][q]=='?'){//cout << "n2";
							grid[i][q] = grid[i][q-1];
							q++;
						}
						else{
							flag2=1;
							q = INT_MAX;
						}
					}
				}
			}
		}
		cout << "Case #" << u+1 << ":" << endl;
		for(lln i=0;i<x;i++){
			for(lln j=0;j<y;j++){
				cout << grid[i][j];
			}
			cout << endl;
		}
	}
	return 0;
} 