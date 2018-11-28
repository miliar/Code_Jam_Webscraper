#include <cstdio>
#include <queue>
using namespace std;

int t,n,k,f[20];

void setF(){
	f[0] = 1LL;
	for(int i=1; i<20; i++) f[i] = f[i-1] + (1<<i);
}

int findX(){
	int i=0;
	for(; i<20; i++) if(k <= f[i]) break;
	return --i;
}

// space and dust
int getSpace(int x){ return (n - f[x])/(1<<(x+1)); }
int getDust(int x){ return (n - f[x])%(1<<(x+1)); }

/*
pair<int,int> getAn(int space){
	pair<int,int> ans;
	ans.first = (space+1)/2 - 1;
	ans.first = space-(space+1)/2;
	return ans;
}*/

void printAnsw(int tc, int space){
	printf("Case #%d: %d %d\n",tc,space-(space+1)/2,(space+1)/2 - 1);
}

int main(){
	//freopen("C-small-2-attempt0.in","r",stdin);
	setF();

	/*k = 15;
	printf("x =%d\n",findX());

	n = 15;
	printf("space = %d, dust =%d\n",getSpace(0),getDust(0));
	printf("space = %d, dust =%d\n",getSpace(1),getDust(1));
	printf("space = %d, dust =%d\n",getSpace(2),getDust(2));
	printf("space = %d, dust =%d\n",getSpace(3),getDust(3));*/

	scanf("%d",&t);

	int x,space,dust;
	for(int tc=1; tc<=t; tc++){
		scanf("%d %d",&n,&k);

		if(k==1){
			space = n;
		}else{
			x = findX();
			space = getSpace(x);
			dust = getDust(x);
			if(k-f[x]<=dust) space++;
		}

		printAnsw(tc,space);
	}

	return 0;
}