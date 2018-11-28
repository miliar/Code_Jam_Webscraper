



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
	int a,T,ok;
	auto fi=fopen("GCJA.txt","w");
	scanf("%d",&T);
	for(a=1;a<=T;a++){
		fprintf(fi,"Case #%d: ",a);
		string st;
		int K,i,j,ans=0;
		vector<int> pan;
		cin>>st;
		scanf("%d",&K);
		for(i=0;i<st.size();i++){
			if(st[i]=='-'){ pan.pub(0); } else{ pan.pub(1); }
		}//11111‚É‚·‚é
		for(i=0;i<st.size()-K+1;i++){
			if(pan[i]==1){continue;}
			ans++;
			for(j=0;j<K;j++){
				pan[i+j]=1-pan[i+j];
			}
		}ok=1;
		for(i=0;i<st.size();i++){
			if(pan[i]==0){
				fprintf(fi,"IMPOSSIBLE\n");
				ok=0;
				break;
			}
		}
		if(ok==1){
			fprintf(fi,"%d\n",ans);
		}
		st.clear();
		pan.clear();
		
	}
	return 0;
}