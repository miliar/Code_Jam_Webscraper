#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

char FC = 0;

struct col{
	char symbol;
	char csymbol;

	int hm;
	int hmc;
	int operator<(const col &o) const{
		if(hm - hmc  == o.hm - o.hmc){
			return symbol == FC;
		}
		return hm - hmc > o.hm - o.hmc;
	}
	string get(){
		string ret(1, symbol);
		--hm;
		while(hmc > 0 && hm > 0){
			ret = ret + csymbol + symbol;
			--hm;
			--hmc;
		}
		if(hm == 0 && hmc == 1){
			ret += csymbol;
			hmc = 0;
		}
		return ret;
	}
};

int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		vector<col> v;
		v.push_back({'B', 'O', B, O});
		v.push_back({'R', 'G', R, G});
		v.push_back({'Y', 'V', Y, V});

		string ret;

		while(ret.size() < N){


			if(!ret.empty()) FC = ret.front();
			sort(v.begin(), v.end());

			bool ok = false;
			for(int i=0; i<v.size(); ++i){
				if(v[i].hm > 0 && ret.back() != v[i].symbol){
					string g = v[i].get();
					if(g.back() == g.front() || g.size() == N){
						ret += g;
					}

					ok = true;
					break;
				}
			}
			if(!ok) break;

		}

		if(ret.size() == N && ret.back() != ret.front()){
			printf("Case #%d: %s\n", tc, ret.c_str());
		}else{
			printf("Case #%d: IMPOSSIBLE\n", tc);

		}



		// RBY - clean
		// RY=>O
		// YB=>G
		// RB=>V




	}
}