#include <bits/stdc++.h>

using namespace std;

char num[55];

void solve(){
	int n, pos = -1, pcur = 0, cnt = 0;
	scanf("%s", num);
	n = strlen(num);
	if(n == 1){
		printf("%s\n", num);
		return;
	}

	for(int i = 0; i < n - 1; i++){
		if(i > 0 && num[i - 1] < num[i])
			pcur = i;
		
		if(num[i] > num[i + 1]){
			pos = pcur;
			break;
		}
	}
	if(pos != -1){
		num[pos]--;
		for(int i = pos + 1; i < n; i++)
			num[i] = '9';
		cnt = 0;
		while(num[cnt] == '0')
			cnt++;
	}
	printf("%s\n", num + cnt);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}
}