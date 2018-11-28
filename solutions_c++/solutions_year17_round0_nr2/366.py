#include<bits/stdc++.h>

using namespace std;

long long N ;
vector < long long > all;

int cal(long long x){
	int ret = 0;
	while(x > 0){
		x /= 10;
		ret++;
	}
	return ret;
}

void back(long long cur){
	if(cur > 0) all.push_back(cur);
	/*----*/
	if(cal(cur) == 18)	return ;
	int last_digit = (cur % 10);
	for(int i = last_digit + (last_digit == 0) ; i <= 9 ; i++)	back(cur * 10 + i);
	
}
void solve(int Tc){
	cin>>N;
	printf("Case #%d: ",Tc);
	int id = upper_bound(all.begin() , all.end() , N) - all.begin() - 1;
	cout<<all[id]<<'\n';
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	back(0);
	sort(all.begin() , all.end());
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++)	solve(i);
}
