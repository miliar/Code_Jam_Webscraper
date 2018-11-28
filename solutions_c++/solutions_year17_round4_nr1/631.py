#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;

int N, P, cnt[9];

void test(int tn){
	memset(cnt, 0, sizeof(cnt));
	for(scanf("%d%d", &N, &P); N--;){
		int a;
		scanf("%d", &a);
		cnt[a%P]++;
	}
	int dap=cnt[0];
	if(P==2) dap+=(cnt[1]+1)/2;
	if(P==3){
		if(cnt[1]>cnt[2]) swap(cnt[1],cnt[2]);
		dap+=cnt[1]+(cnt[2]-cnt[1]+2)/3;
	}
	if(P==4){
		if(cnt[1]>cnt[3]) swap(cnt[1],cnt[3]); // 2x 3y
		dap+=cnt[1], cnt[3]-=cnt[1];
		dap+=cnt[2]/2, cnt[2]%=2;
		if(cnt[2]) dap++, cnt[3]-=2;
		if(cnt[3]>=0) dap+=(cnt[3]+3)/4;
	}
	printf("Case #%d: %d\n", tn, dap);
}

int main(){
	freopen("A-large.in","r",stdin),freopen("output.txt","w",stdout);
	int t, i;
	scanf("%d", &t);
	for(int i=1; i<=t; i++) test(i);
	return 0;
}
