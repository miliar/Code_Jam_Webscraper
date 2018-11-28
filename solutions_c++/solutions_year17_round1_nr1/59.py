#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;
char in[30][30];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++){
			scanf("%s",in[i]);
		}
		for(int i=0;i<a;i++){
			int last=-1;
			int fi=-1;
			for(int j=0;j<b;j++){
				if(in[i][j]!='?'){
					last=in[i][j]-'A';
					if(fi==-1)fi=in[i][j]-'A';
				}
				if(last!=-1)in[i][j]='A'+last;
			}
			for(int j=0;j<b;j++){
				if(fi!=-1&&in[i][j]=='?')in[i][j]=fi+'A';
			}
		}
		int fa=-1;
		int at=-1;
		for(int i=0;i<a;i++){
			if(in[i][0]=='?'){
				if(at!=-1){
					for(int j=0;j<b;j++)in[i][j]=in[at][j];
				}
			}else{
				at=i;
				if(fa==-1)fa=i;
			}
		}
		for(int i=0;i<a;i++){
			if(in[i][0]=='?'){
				for(int j=0;j<b;j++)in[i][j]=in[fa][j];
			}
		}
		printf("Case #%d: \n",t);
		for(int i=0;i<a;i++)printf("%s\n",in[i]);
	}
}