#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int test){
	int n, k; cin >> n >> k;
	vector<bool> stall(n+2, false);
	stall[0] = true; stall[n+1] = true;
	
	int ls = -1, rs = -1;
	int ind = -1;
	
	for(int i = 0; i < k; i++){
		int last = 0;
		ls = -1, rs = -1, ind = -1;
		for(int j = 1; j < n+2; j++){
			if(stall[j]){
				last = j;
				continue;
			}
			
			int lss = j-last-1;
			int rss=0;
			for(int l = j+1; l < n+2; l++){
				if(stall[l]){
					rss = l - j - 1;
					break;
				}
			}
			
			if(ls==-1){
				ls = lss;
				rs = rss;
				ind = j;
				continue;
			}
			if(min(lss,rss) == min(ls,rs)){
				if(max(lss,rss) > max(ls,rs)){
					ls = lss;
					rs = rss;
					ind = j;
					continue;
				}
				continue;
			}
			if(min(lss,rss) > min(ls,rs)){
				ls = lss;
				rs = rss;
				ind = j;
				continue;
			}
		}
		stall[ind] = true;
	}
	
	cout << "Case #" << test << ": " << max(ls,rs) << " " << min(ls,rs) << endl;
}

int main(){
	int t; cin >> t;
	for(int i = 1; i <= t; i++) solve(i);
	return 0;
}
