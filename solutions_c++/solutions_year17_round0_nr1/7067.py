#include <bits/stdc++.h>

using namespace std;

bitset<1000> bs,mask,zero;

int main(){
	zero.reset();
	int t,k,count;
	string str;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		count=0;
		bs.reset();
		mask.reset();
		cin>>str>>k;
		for(int j=0;j<str.size();j++){
			if(str[j]=='+')
				bs[j]=1;
		}
		for(int j=0;j<k;j++){
			mask[j]=1;
		}
		for(int j=0;j<str.size()-k;j++){
			if(bs[0]==0){
				count++;
				bs=(bs & ~mask)|(mask & ~bs);
			}
			bs>>=1;
		}
		if(bs==mask){
			printf("Case #%d: %d\n", i, count);
		}else if(bs==zero){
			printf("Case #%d: %d\n", i, count+1);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}
	return 0;
}