#include <cstdio>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

double side(pair<int, int> a){
	double r=a.first;
	double h=a.second;
	return 2*M_PI*r*h;
}

bool cmp(pair<int,int> a, pair<int,int> b){
	return side(a)<side(b);
}

void solve(){
	int n,k;
	scanf("%d %d",&n,&k);
	vector<pair<int,int>> pancakes;
	for(int i=0; i<n; i++){
		pair<int,int> p;
		scanf("%d %d",&p.first, &p.second);
		pancakes.push_back(p);
	}
	double best=0;
	for(int bottom=0; bottom<n; bottom++){
		double score=0;
		score+=M_PI*pancakes[bottom].first*pancakes[bottom].first
			+side(pancakes[bottom]);
		vector<pair<int,int>> smaller;
		for(int i=0; i<n; i++){
			if(i==bottom){ continue; }
			if(pancakes[i].first<=pancakes[bottom].first){
				smaller.push_back(pancakes[i]);
			}
		}
		if(smaller.size()+1<(size_t)k){
			continue;
		}
		sort(smaller.begin(), smaller.end(), cmp);
		int i=smaller.size()-1;
		int num=1;
		while(num!=k){
			score+=side(smaller[i--]);
			num++;
		}
		if(score>best){best=score;}
	}
	printf("%.9lf\n", best);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int tc=0; tc<t; tc++){
		fprintf(stderr, "%d/%d\n", tc, t);
		printf("Case #%d: ", tc+1);
		solve();
	}
}
