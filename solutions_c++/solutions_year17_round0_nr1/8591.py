#include <bits/stdc++.h>
using namespace std;
int num;
int k;
int vis[2000];
struct state{
	bool v[11];
	int c;
};
state new_state(bool arr[], int cost){
	state n ;
	for(int i = 0 ; i < num ;i++){
		n.v[i] = arr[i];
	}
	n.c = cost;
	return n;
}
queue<state> q;
bool cheCue (bool arr[], int count){
	for(int i = 0 ; i < count ;i++){
		if(arr[i] == 0)
			return 0;
	}
	return 1;
}
int bitArrayToInt32(bool arr[], int count) {
	int ret = 0;
	int tmp;
	for (int i = 0; i < count; i++) {
		tmp = arr[i];
		ret |= tmp << (count - i - 1);
	}
	return ret;
}
int solve(bool s[]){
	memset(vis, -1, sizeof vis);
	while(q.size()){
		q.pop();
	}
	state start = new_state(s,0);
	vis[bitArrayToInt32(s,num)] = 1;
	q.push(start);
	while(q.size()){
		state cur = q.front();
		q.pop();
		if(cheCue(cur.v,num) == 1){
			return cur.c;
		}
		for(int i = 0;i <= num - k;i++){
			bool narr[11];
			for(int j = 0 ; j < num;j++){
				narr[j] = cur.v[j];
				if(j >= i && j < k+i)
					narr[j] = !cur.v[j];
			}
			int decnum= bitArrayToInt32(narr,num);
			if(vis[decnum] == 1)continue;
			vis[decnum] = 1;
			state n = new_state(narr,cur.c+1);
			q.push(n);
		}
	}
	return -1;


}
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	char arr[11];
	bool fstate[11];
	scanf("%d",&t);
	int cnt = 0;
	while(t--){
		cnt++;
		scanf("%s",arr);
		scanf("%d",&k);
		num = strlen(arr);
		for(int i = 0 ; i < num;i++){
			if(arr[i] == '+')
				fstate[i] = 1;
			else
				fstate[i] = 0;
		}
		int ret = solve(fstate);
		if(ret == -1){
			printf("Case #%d: IMPOSSIBLE\n",cnt);
		}else{
			printf("Case #%d: %d\n",cnt,ret);
		}
	}


}
