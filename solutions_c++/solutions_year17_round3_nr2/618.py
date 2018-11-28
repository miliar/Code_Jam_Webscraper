#include <bits/stdc++.h>

#define lld long long

using namespace std;

struct data{
	int x,y,op;
}a[202];
priority_queue<int,vector<int>,greater<int>> q;

void process(){
	int N,M;

	scanf("%d %d",&N,&M);
	int sum = 0,sum2 = 0;
	for(int i=1; i<=N; i++){
        scanf("%d %d",&a[i].x,&a[i].y);
		a[i].op = 1;
		sum += (a[i].y-a[i].x);
	}
	for(int i=1; i<=M; i++){
		scanf("%d %d",&a[i+N].x,&a[i+N].y);
		a[i+N].op = 2;
		sum2 += (a[i+N].y-a[i+N].x);
	}
    sort(a+1,a+N+M+1,[&](data x,data y){
		return x.x < y.x;
    });
    while(!q.empty()) q.pop();
    int ans = 0;
    for(int i=1; i<N+M; i++){
		if(a[i].op != a[i+1].op) ans++;
        if(a[i].op+a[i+1].op == 2) q.push(a[i+1].x-a[i].y);
    }
    if(a[N+M].op + a[1].op == 2) q.push(720*2+a[1].x-a[N+M].y);
    if(a[N+M].op != a[1].op) ans++;
    while(!q.empty()){
        if(sum+q.top() > 720) break;
		sum += q.top(); q.pop();
    }
    ans += (2*q.size());

    while(!q.empty()) q.pop();
    for(int i=1; i<N+M; i++){
        if(a[i].op+a[i+1].op == 4) q.push(a[i+1].x-a[i].y);
    }
    if(a[N+M].op + a[1].op == 4) q.push(720*2+a[1].x-a[N+M].y);
    while(!q.empty()){
        if(sum2+q.top() > 720) break;
		sum2 += q.top(); q.pop();
    }
    ans += (2*q.size());

    printf("%d\n",ans);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		process();
	}

	return 0;
}
