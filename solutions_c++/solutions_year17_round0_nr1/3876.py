#include <bits/stdc++.h>

using namespace std;

char str[1111];
int arr[1111];
queue<int> q;

void solve(){
	while(!q.empty())  // clear queue
		q.pop();

	int n, k, ans = 0;
	scanf("%s%d", str, &k);
	n = strlen(str);

	for(int i = 0; i < n; i++){
		if(str[i] == '-' && q.size() % 2 == 0){
			ans++;
			q.push(i + k - 1);
		}
		if(str[i] == '+' && q.size() % 2 == 1){
			ans++;
			q.push(i + k - 1);
		}
		while(!q.empty() && q.front() == i)
			q.pop();
	}
	if(!q.empty())
		printf("IMPOSSIBLE\n");
	else 
		printf("%d\n", ans);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}
}