/*
TASK: Bathroom
*/
#include <bits/stdc++.h>
using namespace std;
map<long long, long long> m;
int main(){
	int t,i;
	long long n,k,now;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		scanf("%I64d %I64d",&n,&k);
		m.insert(make_pair(n,1));
		while(1){
			map<long long, long long>::iterator it = m.end();	it--;
			k-=(*it).second;
			now = (*it).first;
			now--;
			if(k<=0){
				printf("%I64d %I64d\n",(now/2)+(now%2),now/2);
				break;
			}
			m.erase(it);
			m[now/2]+=(*it).second;
			m[(now/2)+(now%2)]+=(*it).second;
		}
		m.clear();
	}
	return 0;
}
