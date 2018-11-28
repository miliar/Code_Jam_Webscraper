#include <cstdio>
#include <cstring>
using namespace std;

int main(){

	int num;
	scanf("%d",&num);
	for(int i=0;i<num;++i){
		int R,C;
		scanf("%d %d ",&R,&C);
		char str[R][C];
		for(int j=0;j<R;++j){
			for(int k=0;k<C;++k){
				str[j][k] = getchar();
			}	
			getchar();
		}
		int cnt=0,ck=0;
		for(int j=0;j<R;++j){
			for(int k=0;k<C;++k){
				if(str[j][k] == '?'){
					ck=0;
					cnt=0;
					if(k+1<C){
						for(int r=k+1;r<C;++r){
							if(str[j][r] != '?'){
								for(int c=0;c<=cnt;++c)
									str[j][k+c]=str[j][r];
								ck=1;
								break;
							}else{cnt++;}
						}
					}
					if(ck)continue;
					cnt=0;
					if(k-1>=0){
						for(int r=k-1;r>=0;--r){
							if(str[j][r] != '?'){
								for(int c=0;c<=cnt;++c)
									str[j][k+c]=str[j][r];
								ck=1;
								break;
							}else{cnt++;}
						}
					}
				}
			}				
		}
		for(int j=0;j<R;++j){
			for(int k=0;k<C;++k){
				if(str[j][k] == '?'){
					ck=0;
					cnt=0;
					if(j-1>=0){
						for(int r=j-1;r>=0;--r){
							if(str[r][k] != '?'){
								for(int c=0;c<=cnt;++c)
									str[j-c][k]=str[r][k];
								ck=1;
								break;
							}else{cnt++;}
						}
					}
					if(ck)continue;
					cnt=0;
					if(j+1<R){
						for(int r=j+1;r<R;++r){
							if(str[r][k] != '?'){
								for(int c=0;c<=cnt;++c)
									str[j+c][k]=str[r][k];
								ck=1;
								break;
							}else{cnt++;}
						}
					}	
				}
			}				
		}
		printf("Case #%d:\n",i+1);
		for(int j=0;j<R;++j){
			for(int k=0;k<C;++k){
				printf("%c",str[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}
