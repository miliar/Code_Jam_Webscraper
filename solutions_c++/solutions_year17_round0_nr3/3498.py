#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;
typedef unsigned long long int ull;
typedef pair<ull,ull> uu;
class mycomp{
public:
	mycomp(){}
	bool operator()(uu p1, uu p2){
		if(p1.first < p2.first)
			return true;
		else if(p1.first == p2.first)
			return p1.second > p2.second;
		else return false;
	}
};
typedef priority_queue<uu,vector<uu>,mycomp> mypq;
int main(){
	int t;
	ull n, k, j, f, s;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> n >> k;
		mypq spaces;
		j = 0;
		spaces.emplace(n,1);
		while(j < k){
			uu elemen = spaces.top(); spaces.pop();
			f = elemen.first;
			s = elemen.second;
			// printf("%d %d\n", f, s);
			if(f > 2)
				spaces.emplace((f-1)/2,s);
			if(f > 1)
				spaces.emplace(f/2,s+(f-1)/2+1);
			if(++j == k){
				printf("Case #%d: %d %d\n",i,f/2,(f-1)/2);
				break;
			}
		}
	}
	return 0;
}

