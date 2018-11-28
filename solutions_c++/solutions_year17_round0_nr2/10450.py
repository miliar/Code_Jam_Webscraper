#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
bool judge(int n){
	if(n%10==0)return true;
	int pos = n%10;
	n = n/10;
	while(n){
		if(pos<n%10) return true;
		pos = n%10;
		n/=10;
	}
	return false;
}
int main(){
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout)
	int T,ans;
	scanf("%d",&T);
	for(int Case=0;Case<T;Case++){
		scanf("%d",&ans);
		printf("%d\n",ans);
		while(judge(ans))ans--;
		printf("Case #%d: %d\n",Case+1,ans);
	}
}