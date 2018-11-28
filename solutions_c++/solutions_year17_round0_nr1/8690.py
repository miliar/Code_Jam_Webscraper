#include <bits/stdc++.h>

#define is pair<int, string>

using namespace std;

int main(){
	int T;
	cin >> T;
	
	map<string, int> m;
	string s;
	int k, res;
	for(int i = 1; i <= T;++i){
		m.clear();
		res = -1;
		cin.ignore(256, '\n');
		cin >> s >> k;
		int tam = s.size();
		string gab(tam, '+');


		priority_queue<is, vector<is>, greater<is>> p;

		p.push(is(0, s));
		while(!p.empty()){
			auto el = p.top(); p.pop();
			string ne;

			//printf("[%s][%d]\n", el.second.c_str(), el.first);
			if(el.second == gab){
				res = el.first; break;
			}

			for(int j = 0; j <= tam - k; ++j){
				ne = el.second;
				//printf("n1=[%s] & ", ne.c_str());
				for(int h = j; h < j + k; ++h){
					char c = ((ne[h] == '-') ? '+' : '-');
					ne[h] = c;
				}
				//printf("n2=[%s]\n", ne.c_str());
				if(m.find(ne) == m.end()){
					p.push(is(el.first+1, ne));
					m[ne] = 1;
				}
			}
		}
		printf("Case #%d: ", i);
		if(res+1)
			printf("%d\n", res);
		else
			printf("IMPOSSIBLE\n");

	}


	return 0;
}
