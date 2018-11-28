#include<deque>
#include<queue>
#include<map>
#include<string>
#include<iostream>
#include<set>
#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
#define scanf scanf_s
#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pub push_back
using namespace std;
typedef long long int llint;
const llint one = 1;
const llint big = (one<<30);


int main(void){
	int a,T,ok,bef=0,i,j;
	string st;
	char ans[50]={0};
	auto fi=fopen("GCJB.txt","w");
	scanf("%d",&T);
	for(a=1;a<=T;a++){
		ok=0;//not 9 mode
		bef=0;
		fprintf(fi,"Case #%d: ",a);
		cin>>st;
		for(i=0;i<st.size();i++){
			if(bef>st[i]&&ok==0){
				ans[i-1]-=1;
				ok=1;//9 mode
				for(j=i-1;j>0;j--){
					if(ans[j]<ans[j-1]){
						ans[j-1]--;
						ans[j]='9';
					} else{
						break;
					}
				}
			}
			if(ok==1){
				ans[i]='9';
			} else{
				ans[i]=st[i];
			}
			bef=st[i];
		}
		
		for(i=0;i<50;i++){
			if(ans[i]>'0'){ fprintf(fi,"%d",ans[i]-'0'); }
			ans[i]=0;
		}
		fprintf(fi,"\n");
		st.clear();
	}
	return 0;
}
