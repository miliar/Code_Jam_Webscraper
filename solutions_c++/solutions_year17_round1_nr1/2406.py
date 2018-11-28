#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <fstream>

using namespace std;

int main() {
	ifstream cin("al.in");
    ofstream cout("al.out");

	int t, TC, i, j, r, c, k, w;
	char cake[26][26];
	set<char> cant[26];
	
	t = 1;
	cin >> TC;
	
	while( t <= TC ){
		cin >> r >> c;
		
		for( i = 0; i < r; i++ ){
			cant[i].clear();
			for( j = 0; j < c; j++ ){
				cin >> cake[i][j];
				if( cake[i][j] != '?'){
					cant[i].insert( cake[i][j] );
				}
			}
		}
		
		for( i = 0; i < r; i++ ){
			if( cant[i].size() > 0 ){
				for( j = 0; j < c; j++ ){
					if( cake[i][j] != '?' ){
						for( k = j - 1; k >= 0 && cake[i][k] == '?'; k-- ){
							cake[i][k] = cake[i][j];
						}
						for( k = j + 1; k < c && cake[i][k] == '?'; k++ ){
							cake[i][k] = cake[i][j];
						}
					}
				}
				
				for( k = i - 1; k >= 0 && cant[k].size() == 0; k-- ){
					for( w = 0; w < c; w++ ){
						cake[k][w] = cake[i][w];
						cant[k].insert(cake[i][w]);
					}
				}
				
				for( k = i + 1; k < r && cant[k].size() == 0; k++ ){
					for( w = 0; w < c; w++ ){
						cake[k][w] = cake[i][w];
						cant[k].insert(cake[i][w]);
					}
				}
			}
		}
		
		cout << "Case #" << t << ":\n";
		for( i = 0; i < r; i++ ){
			for( j = 0; j < c; j++ ){
				cout << cake[i][j];
			}
			cout << "\n";
		}
		
		t++;
	}
	
	return 0;
}