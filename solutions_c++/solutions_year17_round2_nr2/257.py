#include <bits/stdc++.h>
using namespace std;
const int MAX = 110;
int main(){
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		int yes = 1;
		++cs;
		printf("Case #%d: ", cs);
		int R, O, Y, G, B, V, N; cin >> N;
		scanf("%d%d%d%d%d%d", &R, &O, &Y, &G, &B, &V);
		R = R - G;
		B = B - O;
		Y = Y - V;
		priority_queue<pair<int, pair<int, char> > > q;
		while(!q.empty()) q.pop();
		if(min(B, min(Y, R)) < 0) yes = 0;
		if(B > 0) q.push({B, {B, 'B'}});
		if(R > 0) q.push({R, {R, 'R'}});
		if(Y > 0) q.push({Y, {Y, 'Y'}});
		vector<char> v; v.clear();
		while(!q.empty()){
			auto f = q.top(); q.pop();
			--f.first;
			v.push_back(f.second.second);
			if(q.size()){
				auto s = q.top(); q.pop();
				--s.first;
				v.push_back(s.second.second);
				if(s.first) q.push(s);
			}
			if(f.first) q.push(f);
		}
		for(int i=0; i<v.size(); ++i) if(v[i] == v[i-1]) yes = 0;
		if(v.size() && v[0] == v[v.size() - 1]){
			if(v.size() == 1);
			else yes = 0;
		}

		if(G > 0){
			int ff = 0;
			vector<int> w; w.clear();
			if(R > 0){
				for(auto it:v){
					if(it == 'R' && ff == 0){
						for(int i=1; i<=G; ++i){
							w.push_back('R');
							w.push_back('G');
						}	
						ff = 1;					
					}
					else w.push_back(it);
				}
			}
			else if(R == 0 && N == (G << 1)){
				for(int i=1; i<=G; ++i){
					w.push_back('R');
					w.push_back('G');
				}
			}
			else yes = 1;
			v.clear();
			for(auto it:w) v.push_back(it);
		}

		if(V > 0){
			int ff = 0;
			vector<int> w; w.clear();
			if(Y > 0){
				for(auto it:v){
					if(it == 'Y' && ff == 0){
						for(int i=1; i<=V; ++i){
							w.push_back('Y');
							w.push_back('V');
						}	
						ff = 1;					
					}
					else w.push_back(it);
				}
			}
			else if(Y == 0 && N == (V << 1)){
				for(int i=1; i<=G; ++i){
					w.push_back('Y');
					w.push_back('V');
				}
			}
			else yes = 1;
			v.clear();
			for(auto it:w) v.push_back(it);
		}

		if(O > 0){
			int ff = 0;
			vector<int> w; w.clear();
			if(B > 0){
				for(auto it:v){
					if(it == 'B' && ff == 0){
						for(int i=1; i<=O; ++i){
							w.push_back('B');
							w.push_back('O');
						}	
						ff = 1;					
					}
					else w.push_back(it);
				}
			}
			else if(B == 0 && N == (O << 1)){
				for(int i=1; i<=G; ++i){
					w.push_back('B');
					w.push_back('O');
				}
			}
			else yes = 1;
			v.clear();
			for(auto it:w) v.push_back(it);
		}
		if(v.size() == 0) yes = 0;
		if(yes){
			for(auto it:v){
				printf("%c", it);
			}
			printf("\n");
		}
		else printf("IMPOSSIBLE\n");
		// cin >> R >> O >> Y >> G >> B >> Y;
	}	
}