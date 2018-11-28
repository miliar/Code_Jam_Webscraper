#include<bits/stdc++.h>
using namespace std;
int main(){
//freopen("input.in","r",stdin);
//freopen("output.in","w",stdout);
int test,t;
cin>>test;
t=test;
int n;
double pos,speed,dest,max_time = 0,cal_time;
while(test--){
	cin>>dest>>n;
	max_time = 0;
	while(n--){
		cin>>pos>>speed;
		cal_time = (dest - pos)/speed;
		max_time = max(max_time, cal_time);
	}
	printf("Case #%d",t-test);
	if(max_time > 0){
		printf(": %.6f\n",dest/max_time);
	}
	else
		printf(": %.6f\n",dest);
}
return 0;
}
