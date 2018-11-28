#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <iomanip>
#include <map>

using namespace std;



int main(){
	int q;
	cin >> q;
	for (int z = 0; z < q; z++){
		set <int> row[30];
		set <int> col[30];
		string cake[30];

		int r, c;
		cin >> r >> c;
		
		for (int i = 0; i < r; i++){
			cin >> cake[i];
		}
		
		int total = 0;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (cake[i][j] != '?'){
					total++;
					row[cake[i][j] - 'A'].insert(i);
					col[cake[i][j] - 'A'].insert(j);
				}
			}
		}
		
		for (int i = 0; i < 26; i++){
			if (col[i].size()> 0){
				int left = *(col[i].begin());
				int right = *(col[i].rbegin());
				int pre = *(col[i].begin()) -1;
				vector <int> missCol;
				for (auto it = col[i].begin(); it != col[i].end(); it++){
					if (*it != pre+1){
						for (int j = pre+1; j < *it; j++){
							missCol.push_back(j);
						}
					}
					pre = pre+1;
				}
				if (missCol.size() != 0){
					for (int k = 0; k < missCol.size(); k++){
						for (auto it = row[i].begin(); it != row[i].end(); it++){
							cake[*it][k] = char(i+'A');
							total++;
						}
					}
				}
				bool good = true;
				while (good){
					if (left > 0){
						for (auto it = row[i].begin(); it != row[i].end(); it++){
							if (cake[*it][left-1] != '?'){
								good = false;
								break;
							}
							col[i].insert(left-1);
						}
						if (good){
							for (auto it = row[i].begin(); it != row[i].end(); it++){
								cake[*it][left-1] = char(i+'A');
								total++;
							}
							left--;
						}
					}else {
						good = false;
					}
				}
				good = true;
				while (good){
					if (right < c-1){
						for (auto it = row[i].begin(); it != row[i].end(); it++){
							if (cake[*it][right+1] != '?'){
								good = false;
								break;
							}
						}
						if (good){
							for (auto it = row[i].begin(); it != row[i].end(); it++){
								cake[*it][right+1] = char(i+'A');
								total++;
							}
							col[i].insert(right+1);
							right++;
						}
					}else {
						good = false;
					}
				}
			}
			if (row[i].size() > 0){
				int up = *(row[i].begin());
				int low = *(row[i].rbegin());
				int pre = *(row[i].begin()) -1;
				vector <int> missRow;
				for (auto it = row[i].begin(); it != row[i].end(); it++){
					if (*it != pre+1){
						for (int j = pre+1; j < *it; j++){
							missRow.push_back(j);
						}
					}
					pre = pre+1;
				}
				if (missRow.size() != 0){
					for (int k = 0; k < missRow.size(); k++){
						for (auto it = col[i].begin(); it != col[i].end(); it++){
							cake[k][*it] = char(i+'A');
							total++;
						}
					}
				}
				bool good = true;
				while (good){
					if (up > 0){
						for (auto it = col[i].begin(); it != col[i].end(); it++){
							if (cake[up-1][*it] != '?'){
								good = false;
								break;
							}
						}
						if (good){
							for (auto it = col[i].begin(); it != col[i].end(); it++){
								cake[up-1][*it] = char(i+'A');
								total++;
							}
							row[i].insert(up-1);
							up--;
						}
					} else {
						good = false;
					}
				}
				good = true;
				while (good){
					if (low < r-1){
						for (auto it = col[i].begin(); it != col[i].end(); it++){
							if (cake[low+1][*it] != '?'){
								good = false;
								break;
							}
						}
						if (good){
							for (auto it = col[i].begin(); it != col[i].end(); it++){
								cake[low+1][*it] = char(i+'A');
								total++;
							}
							row[i].insert(low+1);
							low++;
						}
					}else {
						good = false;
					}
				}
			}
			
		}
		
		
		cout << "Case #" << z+1 << ": " << endl;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
}