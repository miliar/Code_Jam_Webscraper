#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main(){
	int t;
	cin >> t;
	int r, c;
	for(int it = 0; it < t; it ++){		
		cin >> r >> c;
		char a[r][c];
		
		for(int i = 0; i < r; i ++){
			for(int j = 0; j < c; j ++){
				cin >> a[i][j];
			}
		}
		
		for(int i = 0; i < r; i ++){
			vector<pair<int, char> > temp;
			for(int j = 0; j < c; j ++){
				if(a[i][j] != '?')temp.push_back(make_pair(j, a[i][j]));
			}
			if(temp.size() == 0)continue;
			for(int k = 0; k < temp[0].first; k ++)a[i][k] = temp[0].second;
			for(int k = 1; k < temp.size(); k ++){
				for(int l = temp[k - 1].first + 1; l < temp[k].first; l ++)a[i][l] = temp[k].second; 
			}
			for(int l = temp[temp.size() - 1].first + 1; l < c; l ++)a[i][l] = temp[temp.size() - 1].second;
		}
		
		int index = 0;
		while(a[index][0] == '?')index ++;
		for(int i = 0; i < index; i ++){
			for(int j = 0; j < c; j ++)a[i][j] = a[index][j];
		}
		
		for(int i = index + 1; i < r; i ++){
			if(a[i][0] != '?')continue;
			for(int j = 0; j < c; j ++)a[i][j] = a[i-1][j];
		}
		
		cout << "Case #" << it + 1 << ": " << endl;
		
		for(int i = 0; i < r; i ++){
			for(int j = 0; j < c; j ++){
				cout << a[i][j];
			}
			cout << endl;
		}
	}
	return 0;
} 
