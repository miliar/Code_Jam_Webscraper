#include <iostream>
#include <string>
#include <stdio.h>
#include <map>
#include <deque>
using namespace std;

struct D{
	std::string str;
	int count;
};

inline bool isComplete(string& str){
	for(int i=0;i<(int)str.size();++i)
		if(str[i] == '-') return false;
	return true;
}

int getAns(string str, int k){
	if(isComplete(str)) return 0;

	int n = str.size();
	map<string, bool> vis;
	deque<D> q;

	D d; d.str = str; d.count = 0;
	q.push_back(d); vis[str] = true;
	while(!q.empty()){
		D now = q.front(); q.pop_front();
		for(int i=0;i<=n-k;++i){
			string p = now.str;
			for(int j=i;j<i+k;++j){
				if(p[j] == '-') p[j] = '+';
				else p[j] = '-';
			}
			if(isComplete(p)) return now.count + 1;
			else if(vis.find(p) == vis.end()){
				D nd; nd.str = p; nd.count = now.count + 1;
				q.push_back(nd); vis[p] = true;
			}
		}
	}
	return -1;	
}

int main(){
	int test; cin>>test;
	for(int t=1;t<=test;++t){
		string str; cin>>str;
		int k; cin>>k;
		int ans = getAns(str, k);
		if(ans >= 0){
			cout << "Case #" << t << ": " << ans << endl;
		}else{
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
