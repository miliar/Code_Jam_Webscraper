#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<set>
#include<string>
#include<map>
#include<stdlib.h>

using namespace std;
#define INF 0x3f3f3f3f

typedef long long LL;

char s[1010];

struct Interval{
	int ls,rs;
	Interval(){}
	Interval(int a,int b){
		if(a > b)
			swap(a,b);
		ls = a;
		rs = b;
	}
	Interval(int n){
		if(n % 2 == 1){
			ls = rs = (n + 1) / 2;
		}else{
			ls = n / 2;
			rs = ls + 1;
		}
	}
	bool operator<(Interval x) const{
		if(ls != x.ls)
			return ls < x.ls;
		return rs < x.rs;
	}
};



pair<int,int> solve(int n,int k){
	priority_queue<Interval> q;
	q.push(Interval(n));
	for(int i = 1;i < k;++i){
		Interval now = q.top();
		q.pop();
		int left = now.ls - 1,
			right = now.rs - 1;
		Interval a(left);
		Interval b(right);
		if(a < b){
			q.push(b);
			q.push(a);
		}else{
			q.push(a);
			q.push(b);
		}
	}
/*	if(q.front().ls == 0){
		printf("q: %zu\n",q.size());
		while(!q.empty()){
			printf("%d %d\n",q.front().rs,q.front().ls);
			q.pop();
		}
		return make_pair(-1,-1);
	}*/
	return make_pair(q.top().rs - 1,q.top().ls - 1);
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int n,k;
		scanf("%d%d",&n,&k);
		pair<int,int> ans = solve(n,k);
		printf("Case #%d: %d %d\n",cas,ans.first,ans.second);
	}
	return 0;
}

