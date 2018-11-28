#include <bits/stdc++.h>
using namespace std;

#define IOS std::ios_base::sync_with_stdio(false);std:cin.tie(0);std::cout.tie(0);
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {

	int casos;
	cin >> casos;
	for(int caso = 1; caso <= casos; caso++) {
		cout << "Case #" << caso << ": " << endl;

		int r, c;
		vector<string> vec;
		bool vis[100][100];
		memset(vis, 0, sizeof vis);
		cin >> r >> c;
		string s;
		for(int i = 0; i < r; i++) {
			cin >> s;
			vec.push_back(s);
		}

		for(int i = 0; i < r; i++) {
			for(int k = 0; k < c; k++) {
				char let = vec[i][k];
				if(let == '?') continue;
				if(vis[i][k]) continue;

				int left = k, right = k;
				for(left = k-1; left >= 0 && vec[i][left] == '?'; left--) 
					vec[i][left] = let, vis[i][left]= true;
				left++;
				for(right = k+1; left < c && vec[i][right] == '?'; right++) 
					vec[i][right] = let, vis[i][right] = true;
				right--;

				bool can = true;
				int top = i + 1;
				for(top = i+1; top < r; top++) {
					for(int m = left; m<=right; m++)
						if(vec[top][m] != '?') can = false;
					if(!can) {
						break;
						//top++;
					}
					for(int m = left; m<=right; m++)
						vec[top][m] = let, vis[top][m] = true;
				}
				can = true;
				for(top = i-1; top >= 0; top--) {
					for(int m = left; m<=right; m++)
						if(vec[top][m] != '?') can = false;
					if(!can) {
						break;
						//top++;
					}
					for(int m = left; m<=right; m++)
						vec[top][m] = let, vis[top][m] = true;
				}
			}

		}

		for(int i = 0; i < r; i++)
			cout << vec[i] << endl;

	}

	return 0;
}
