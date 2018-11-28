#include <iostream>
#include <cmath>
#include <memory>
#include <utility>
#include <cstdint>
#include <cfloat>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <random>
#include <sstream>
#include <iterator>
#include <ostream>


using namespace std;

int main() {

	int T,K; char *Sraw=new char[2000];
	vector<bool> S;
	S.clear();
	int casee=1;
	cin>>T;
	for(;T;T--,casee++){
		int N=0;
		scanf("%s%d",Sraw,&K);
		for(size_t c=0;Sraw[c];c++){
			switch(Sraw[c]){
			case '-':S.emplace_back(false); break;
			case '+':S.emplace_back(true); break;
			}
		}

		auto OP=[K=K](auto from){
			for(auto TT=K;TT;TT--,from++){
				*from=!*from;
			}

		};
		auto it=S.begin();
		for(; S.end()-it>=K; it++ ){
			if(!*it) {
				OP(it);
				N++;
			}
		}

		for(; it!=S.end()&&*it; it++);

		if(it==S.end()){
			printf("Case #%d: %d\n",casee,N);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",casee);
		}
		//cout<<i
		S.clear();
	}
	return 0;
}
