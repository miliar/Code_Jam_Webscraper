#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int R[100];
int Q[100][100];

vector<pair<int,int> > counts[52];

int main(){
	int T;
	cin >> T;
	
	for(int t = 0; t < T; t++){
		int N,P;
		cin >> N >> P;
		
		for(int i = 0; i < N; i++){
			cin >> R[i];
		}
		
		for(int i = 0; i < 52; i++){
			counts[i].clear();
		}
		
		
		
		for(int i = 0; i < N; i++){
			for(int j = 0; j < P; j++){
				cin >> Q[i][j];
			}
		}
		
		for(int i = 0; i < N; i++){
			for(int j = 0; j < P; j++){
				int l = 1000000;
				int r = 1;
				for(int k = 1; k <= 1000000; k++){
					if (Q[i][j] < R[i] * k - R[i] * k / 10){
						break;
					}
					else if (Q[i][j] <= R[i] * k + R[i] * k / 10 &&
						Q[i][j] >= R[i] * k - R[i] * k / 10){
						l = min(l, k);
						r = max(r, k);
					}
				}
				if (l > r){
					l = -1;
					r = -1;
				} else {
					counts[i].push_back(make_pair(l,r));
				}
			}
		}
		
		for(int i = 0; i < N; i++){
			sort(counts[i].begin(), counts[i].end());
		}
		
		int answer = 0;
		while(true){
			for(int i = 0; i < N; i++){
				if (counts[i].size() == 0) goto out;
			}
			pair<int,int> range = counts[0].back();
			bool good = true;
			for(int i = 1; i < N; i++){
				if (counts[i].back().first <= range.second && counts[i].back().second >= range.first){
					range = {max(range.first, counts[i].back().first), min(range.second, counts[i].back().second)};
				} else if (counts[i].back().first > range.second){
					counts[i].pop_back();
					good = false;
					break;
				} else if (counts[i].back().second < range.first){
				
					good = false;
					for(int j = 0; j < i; j++){
						if (counts[j].back().first > counts[i].back().second){
							counts[j].pop_back();
						}
					}
				}
			}
			
			if (good) answer++;
			else {
				continue;
			}
			for(int i = 0; i < N; i++){
				counts[i].pop_back();
			}
		}
		
		out:;
		
		
	
		cout << "Case #" << t+1 << ": " << answer << endl;
	}
}