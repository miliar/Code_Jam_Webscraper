#include<bits/stdc++.h>
using namespace std;

#define MAX 1009

char str[MAX];

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,tt,n,i,j,k;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%s",str);
		scanf("%d",&k);
		n=strlen(str);
		int result_flag=1;
		int flip_cnt=0;
		for(i=0;i<n;++i){
			if(str[i]=='-'){
			int cnt=0;
			for(j=i;j<n;++j){
				if(str[j]=='+')
					break;
				if(str[j]=='-')
					++cnt;
			}
			if(cnt>=k){
				++flip_cnt;
				for(j=i;j<i+k;++j){
					str[j]='+';
				}
				i=i+k-1;
			}
			else{
				++flip_cnt;
				int cnt_bits=0;
				for(j=i;j<i+k&&j<n;++j){
					++cnt_bits;
					if(str[j]=='+')
						str[j]='-';
					else
						str[j]='+';
				}
				if(cnt_bits==k){
					i=i+cnt-1;
				}
				else{
					result_flag=0;
					i=n-1;
				}	
			}
		}
		//printf("%s\n",str);
	}
	printf("Case #%d: ",tt);
	if(!result_flag)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n",flip_cnt);
	}
	return 0;
}
