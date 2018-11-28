#include <bits/stdc++.h>
using namespace std;

bool valid(char[]);
int getNi(char[]);
long long getNum(char[]);
long long qPow(long long,int);
int sz;

int main(){
	int t;scanf("%d",&t);
	for(int i=1;i<=t;i++){
		char ss[20];scanf("%s",ss);
		sz=strlen(ss);
		if(!valid(ss)){
			int ff=getNi(ss);int jjj;
			for(int i=0;i<sz;i++){
				if(ss[i]==ss[ff-1]){
					jjj=i+1;
					break;
				}
			}
			for(int i=jjj;i<sz;i++)ss[i]='9';
			long long jizz=getNum(ss);
			jizz-=qPow(10,sz-jjj);
			printf("Case #%d: %lld\n",i,jizz);
		}else{
			printf("Case #%d: %s\n",i,ss);
		}
	}
	return 0;
}

bool valid(char x[]){
	int b=-1;
	for(int i=0;i<sz;i++){
		if(x[i]<b)return 0;
		else b=x[i];
	}
	return 1;
}

int getNi(char x[]){
	int b=-1;
	for(int i=0;i<sz;i++){
		if(x[i]<b) return i;
		b=x[i];
	}
}

long long getNum(char x[]){
	long long r=0;
	for(int i=0;i<sz;i++)
		r=(x[i]-'0')+r*10;
	return r;
}

long long qPow(long long a,int n){
	long long rr=1;
	while(n){
		if(n&1) rr*=a;
		n>>=1;
		a*=a;
	}
	return rr;
}