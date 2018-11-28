#include <cstdio>
#define LL long long
using namespace std;

LL num;

LL str[25];
int top=0;

inline void solve(int T){
	printf("Case #%d: ",T);
	scanf("%lld",&num);

	top=0;
	while(num!=0){
		str[++top]=num%10;
		num/=10;
	}

	int pos;
	for (pos=top;pos>1;pos--){
		if (str[pos]<=str[pos-1]) continue;
		break;
	}

	if (pos==1){
		num=0;
		for (int i=top;i>=1;i--) num=num*10LL+str[i];
		printf("%lld\n",num);
		return;
	}


	for (;pos<=top;pos++){
		if (pos==top || str[pos+1]<=str[pos]-1){
			str[pos]--;
			break;
		}
	}

	for (int i=pos-1;i>=1;i--) str[i]=9;

	num=0;
	for (int i=top;i>=1;i--) num=num*10LL+str[i];
	printf("%lld\n",num);
	return;
}

int main(){
	freopen("B-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T=0;scanf("%d",&T);
	for (int i=1;i<=T;i++)
		solve(i);
	return 0;
}