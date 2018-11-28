#include <algorithm>
#include <cstdio>
#define t_max 100
#define s_max 1000000000
#define n_max 1005
#define long long ll
using namespace std;

double horse[n_max][2];
int T;
double D, N;

double t_bound = -1;

void parse(){
	for(int i = 0; i < N; i++){
		double pos, speed;
		scanf("%lf %lf", &pos, &speed);
		double time = (D - pos)	/ speed;
		t_bound = max(t_bound, time);
		//printf("t_bound %lf\n", t_bound);
	}
}

void init(){
	t_bound = -1;
}

int main(){
	scanf("%d", &T);
	for(int i = 0; i < T; i++){
		init();
		scanf("%lf %lf", &D, &N);
		parse();
		printf("Case #%d: %lf\n",i+1, D / t_bound);
	}
}


