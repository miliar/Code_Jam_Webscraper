#include<bits/stdc++.h>
using namespace std;
int buf, debuf, hp;
int dp[101][101][101][101];
int d(int my_hp, int my_att, int you_hp, int you_att){
	if(my_att >= you_hp)return 1;
	int&res = dp[my_hp][my_att][you_hp][you_att];
	if(res != -1)return res;
	res = 1000000000;
	if(hp > you_att){
		res = min(res, d(hp - you_att, my_att, you_hp, you_att) + 1);
	}
	if(my_hp > you_att){
		res = min(res, d(my_hp - you_att, my_att, you_hp - my_att, you_att) + 1);
	}
	if(my_hp > you_att){
		res = min(res, d(my_hp - you_att, my_att+buf, you_hp, you_att) + 1);
	}
	int att2 = max(you_att - debuf,0);
	if(my_hp > att2){
		res = min(res, d(my_hp - att2, my_att, you_hp, att2) + 1);
	}
	return res;
}
int main(){
	int _,t;
	int my_hp, my_att, you_hp, you_att;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d%d%d%d%d",&my_hp, &my_att, &you_hp, &you_att, &buf, &debuf);
		hp = my_hp;
		memset(dp,-1,sizeof(dp));
		int w = d(my_hp, my_att, you_hp, you_att);
		printf("Case #%d: ",t);
		if(w == 1000000000)puts("IMPOSSIBLE");else
			printf("%d\n",w);
	}
	return 0;
}
