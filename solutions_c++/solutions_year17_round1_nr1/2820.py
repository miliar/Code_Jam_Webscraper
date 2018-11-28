/*
 * cake.cc
 *
 *  Created on: Apr 15, 2017
 *      Author: maciek
 */
#include <iostream>
#include <vector>
#include <map>


using namespace std;


int main(){
	int T;
	char c;
	cin >> T;

	for(int i = 0; i < T; i++){
		int R, C;
		cin >> R >> C;
		vector< vector<char> > G(R, vector<char>(C));
		map<char, pair<int,int> > L;
		map<char, pair<int, int> > limit;
		//cout << "*****" << endl;
		for(int j = 0; j < R; j++){
			for(int k = 0; k < C; k++){
			cin >> c;
			G[j][k] = c;
			//cout << c;
			if(c != '?')
				L[c] = pair<int,int>(j,k);
			}
			//cout << endl;
		}

		for(map<char, pair<int,int> >::iterator it = L.begin(); it != L.end(); it++){
			//cout << it->first << " " << it->second.first << " " << it->second.second << endl;
			int posR = it->second.first;
			int posC = it->second.second;
			int y = posC+1;
			while(y < C && G[posR][y] == '?'){
				G[posR][y] = it->first;
				//cout << it->first << posR << " " << y << endl;
				y++;
			}
			int ymax = y-1;
			y = posC-1;
			while(y >= 0 && G[posR][y] == '?'){
				G[posR][y] = it->first;
				//cout << it->first << posR << " " << y << endl;
				y--;
			}
			int ymin = y+1;
			limit[it->first] = pair<int,int>(ymin,ymax);
		}

		for(map<char, pair<int,int> >::iterator it = L.begin(); it != L.end(); it++){
			int posR = it->second.first;
			int posC = it->second.second;
			int x = posR-1;
			while(x >= 0){
				bool free = true;
				for(int j = limit[it->first].first; j <= limit[it->first].second; j++)
					if(G[x][j] != '?'){
						free = false;
						break;
					}
				if(free){
					for(int j = limit[it->first].first; j <= limit[it->first].second; j++)
						G[x][j] = it->first;
					x--;
				}else{
					break;
				}
			}

			x = posR+1;
			while(x < R){
				bool free = true;
				for(int j = limit[it->first].first; j <= limit[it->first].second; j++)
					if(G[x][j] != '?'){
						free = false;
						break;
					}
				if(free){
					for(int j = limit[it->first].first; j <= limit[it->first].second; j++)
						G[x][j] = it->first;
					x++;
				}else{
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << endl;
		for(int j = 0; j < R; j++){
			for(int k = 0; k < C; k++)
				cout << G[j][k];
			cout << endl;
		}
	}
}



