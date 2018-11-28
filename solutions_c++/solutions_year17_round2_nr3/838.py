#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>

using namespace std;

int T, N, M, K, D, S, Q;
int U, V;

int dist[103][103];
struct Horse{
	int sp;
	int mx;
} h[103];

double res[103];
int done[103];

int main(){
	cin>>T;
	for(int cs =1; cs<=T; ++cs){
		cin>>N>>Q;
		for (int i =0; i<N; ++i)
			cin>>h[i].mx>>h[i].sp;
		for(int i = 0; i<N; ++i)
			for(int j = 0; j < N; ++j)
				cin>>dist[i][j];

		for(int q = 0; q < Q; ++q){
			cin>>U>>V;
			--U;
			--V;
		}
		for(int i =0; i<N; ++i){
			res[i] = 1e128;
			done[i] = 0;
		}

		multimap<double,Horse> dyn[103];
		dyn[0].insert(make_pair(0.0, h[0]));

		for(int i = 0; i<N-1; ++i){
			if(i){
				// printf("%d\n", dyn[i].size());
				dyn[i].insert(make_pair(dyn[i].begin()->first, h[i]));
				// puts("good");
				// printf("%d\n", dyn[i].size());
			}
			for(map<double, Horse>::iterator iter= dyn[i].begin(); iter != dyn[i].end(); ++iter){
				if(iter->second.mx >= dist[i][i+1]){
					Horse nh;
					nh.mx = iter->second.mx - dist[i][i+1];
					nh.sp = iter->second.sp;
					double newtime = iter->first + (double)dist[i][i+1]/iter->second.sp;
					dyn[i+1].insert(make_pair(newtime , nh));
				}
			}
		}
		// cout<<dyn[N-1].size()<<endl;
		printf("Case #%d: %.7f\n",cs, dyn[N-1].begin()->first);
	}
}
