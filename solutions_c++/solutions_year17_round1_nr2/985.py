#include <cstdio>
#include <vector>
#include <set>

using namespace std;

void solve(){
	int n, p;
	scanf("%d %d", &n, &p);
	vector<int> needed;
	for(int i=0; i<n; i++){
		int x;
		scanf("%d", &x);
		needed.push_back(x);
	}
	vector<multiset<int>> parts;
	for(int i=0; i<n; i++){
		multiset<int> pp;
		for(int j=0; j<p; j++){
			int x;
			scanf("%d", &x);
			pp.insert(x);
		}
		parts.push_back(pp);
	}
	int cnt=0;
	for(int target=0; target<1234567; target++){
		bool too_small=false;
		bool too_big=false;
		for(int i=0; i<n; i++){
			if(parts[i].size()==0){ too_small=true; break; }
			int question=*(parts[i].begin());
			//printf("Q: %d\n", question);
			if(target*11*needed[i]<10*question){
			   	too_small=true; 
				break;
			}
			if(target*9*needed[i]>10*question){
				parts[i].erase(parts[i].begin());
			   	too_big=true; 
				target--;
				break;
			}
		}
		//printf("Target=%d, small:%d, big:%d\n", target, too_small, too_big);
		if(too_small || too_big){}
		else{
			cnt++;
			for(int i=0; i<n; i++){
				parts[i].erase(parts[i].begin());
			}
			target--;
		}
	}
	printf("%d\n", cnt);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int tc=0; tc<t; tc++){
		printf("Case #%d: ", tc+1);
		solve();
	}
}
