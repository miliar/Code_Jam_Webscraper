#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<math.h>

#define ll long long
using namespace std;

int n;
char c[107];

ll toint(){
	ll x=0;
	for(int i=0;i<n;i++){
		x*=10;
		x+=c[i]-'0';
	}
	return x;
}

int check(){
	for(int i=1;i<n;i++){
		if(c[i]<c[i-1]){
			return 0;
		}
	}
	return 1;
}


void dec(int x){
	c[x]--;
	if(c[x]<'0'){
		c[x]='9';
		dec(x-1);
	}
}

void inc(int x){
	c[x]++;
	if(c[x]>'9'){
		inc(x-1);
	}
}

void sol(){
	int i,j;
	scanf("%s",&c);
	n=strlen(c);
	if(check()){
		printf("%s\n",c);
		return;
	}
	ll ans=-1;
	for(i=n-1;i>0;i--){
		dec(i-1);
		c[i]='9';
		if(check()){
			ans=max(ans,toint());
		}
	}
	printf("%I64d\n",ans);
}

int main(){
#pragma comment(linker, "/STACK:1073741824")
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#else
	//freopen("input_file.txt","r",stdin);
	//freopen("output_file.txt","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		sol();
	}
	return 0;
}