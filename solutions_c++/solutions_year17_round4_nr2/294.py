#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <unordered_map>

Federico Javier Pousa

int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		int N, C, M, Ps[1005], Bs[1005], resu[1005], cant[1005];
		memset(resu, 0, sizeof resu);
		memset(cant, 0, sizeof cant);
		cin >> N >> C >> M;
		for(int i=0; i<M; i++){
			cin >> Ps[i] >> Bs[i];
			Ps[i]--;
			resu[Ps[i]]++;
			cant[Bs[i]]++;
		}
		int inf = 0;
		for(int i=0; i<1005; i++){
			inf = max(inf, cant[i]);
		}
		if(inf)inf--;
		int sup = 1002;
		int promo = 0;
		while(inf+1!=sup){
			int med = (inf+sup)/2;
			bool puedo = true;
			int promoact = 0;
			int acum = 0;
			for(int i=0; i<N; i++){
				acum += resu[i];
				if(acum>med*(i+1)){
					puedo = false;
					break;
				}
				promoact += max(0, resu[i]-med);
			}
			if(puedo){
				sup = med;
				promo = promoact;
			}else{
				inf = med;
			}
		}
		cout << "Case #" << caso << ": " << sup << " " << promo << endl;
	}
	return 0;
}
