#include <bits/stdc++.h>

typedef unsigned long long ull;

ull chk(ull num){
	ull revnum = 0,cnt = 0;
	while(num){
		int d = num%10;
		revnum*=10;
		revnum+=d;
		num/=10;
		cnt++;
	}
	num = 0;

	int fg = 0;
	int pd = 0;
	int c = 0;
	while(c<cnt){
		c++;
		int d = revnum%10;
		if(fg){
			d = 0;
			num*=10;
			num+=d;
			revnum/=10;
			continue;
		}
		if(pd>d){
			fg = 1;
			d = 0;
		}
		num*=10;
		num+=d;
		revnum/=10;
		pd = d;
	}

	return num;
}

int main(){
	int tc=1,t;
	scanf("%d",&t);
	while(tc<=t){
		ull num,ans;
		scanf("%llu",&num);
		while(1){
			if(num){
				if(num%10==0)num--;
			}
			ans = chk(num);
			if(ans == num)break;
			num = ans;
		}
		printf("Case #%d: %llu\n",tc,ans );
		tc++;
	}
}