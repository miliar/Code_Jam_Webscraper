#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define mp make_pair
#define ll long long
#define pb push_back
#define vi vector<ll>



int main() {
	int q;
	cin >> q;
	

	for(int z=1; z<=q; z++){
		vector<vector<char>> v;
		int r, c;
		cin >> r >> c;
		for(int i=0; i<r; i++){
			vector<char> u;
			for(int j=0; j<c; j++){
				char x;
				cin >> x;
				u.pb(x);
			}
			v.pb(u);
		}
		for(int i=0; i<r; i++){
			
			for(int j=0; j<c; j++){
				if(j<c-1 && v[i][j+1]=='?' && v[i][j]!='?'){
					v[i][j+1]=v[i][j];
				}
				if(j>0 && v[i][j-1]=='?' && v[i][j]!='?'){
					v[i][j-1]=v[i][j];
					j-=2;
					continue;
				}
			}
		}
		for(int i=0; i<c; i++){
			
			for(int j=0; j<r; j++){
				if(j<r-1 && v[j+1][i]=='?' && v[j][i]!='?'){
					v[j+1][i]=v[j][i];
				}
				if(j>0 && v[j-1][i]=='?' && v[j][i]!='?'){
					v[j-1][i]=v[j][i];
					j-=2;
					continue;
				}
			}
		}
		cout << "Case #" << z << ":" << endl; 
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				cout << v[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}