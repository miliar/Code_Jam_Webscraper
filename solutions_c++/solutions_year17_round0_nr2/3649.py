#include<bits/stdc++.h>
using namespace std;

vector<int>T;

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,tt,i,j,start_index;
	long long int n;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%lld",&n);
		long long int temp=n;
		while(temp>0){
			int dig=temp%10;
			temp=temp/10;
			T.push_back(dig);
		}
		reverse(T.begin(),T.end());
		for(i=1;i<T.size();++i){
			if(T[i]<T[i-1]){
				if(i==1){
					T[0]=T[0]-1;
					for(i=1;i<T.size();++i)
						T[i]=9;
				}
				else{
					j=i;
					--T[j-1];
					while((j-1>=1)&&(T[j-1]<T[j-2])){
						--T[j-2];
						T[j-1]=9;
						j=j-1;
						
					}
					for(j=i;j<T.size();++j)
						T[j]=9;
				}
				break;
			}
		}
		for(i=0;i<T.size();++i){
			if(T[i]!=0){
				start_index=i;
				break;
			}
		}
		for(i=1;i<start_index;++i)
			T[i]=9;
		printf("Case #%d: ",tt);
		for(i=0;i<T.size();++i)
			if(T[i]!=0) printf("%d",T[i]);
		printf("\n");
		T.clear();
	}
	return 0;
}
