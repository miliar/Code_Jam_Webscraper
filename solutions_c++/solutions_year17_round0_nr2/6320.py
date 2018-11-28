#include <cstdio>
#include <cstring>

void solve(){ 
	char c[1024];
	int l;
	char* begin;
	scanf("%s",c);
	l=strlen(c);
	for(int i=0;i<l;i++){
		c[i]-='0';
	}
	bool change=true;
	while(change){
		change=false;
		for(int i=0;i<l-1;i++){
			if(c[i]>c[i+1]){
				change=true;
				c[i]--;
				for(int j=i;c[j]<0;j--){
					c[j]=9;
					c[j-1]--;
				}
				for(int j=i+1;j<l;j++){
					c[j]=9;
				}
			}
		}
	}
	for(int i=0;i<l;i++){
		c[i]+='0';
	}
	begin=c+l-1;
	for(int i=0;i<l;i++){
		if(c[i]!='0'){
			begin=c+i;
			break;
		}
	}
	printf("%s\n",begin);
}
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}
