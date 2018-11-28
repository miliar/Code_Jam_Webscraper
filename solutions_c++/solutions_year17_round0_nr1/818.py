#include<iostream>
#include<stdio.h>
#include<string.h>
#include <algorithm>
#define FR(i,a,b) for(i=a;i<b;++i)
#define FRS(i,a,b,s) for(i=a;i<b;i+=s)
#define FRE(i,a,b) for(i=a;i<=b;++i)
#define FRES(i,a,b,s) for(i=a;i<=b;i+=s)
// 0->tt-1		FR(i, 0, tt) printf(" 1");
// 0,2,4->tt-1	FRS(i, 0, tt, 2) printf(" 2");
// 0->tt		FRE(i, 0, tt) printf(" 3");
// 0,2,4->tt	FRES(i, 0, tt, 2) printf(" 4");
using namespace std;

int i, j;
long long n, k;
int tt;
string s;
	
void run(){
	cin >> s >> k;
	bool ok = true;
	//for(int i=0; i<s.length; i++)
	n=0;
	FR(i, 0, s.length())
	{
		if(s[i]=='-' && i+k <= s.length()){
			FR(j,i,i+k){
				if(s[j] =='-') s[j] = '+';
				else s[j] ='-';
			}
			n++;
		}
		if(s[i]=='-') ok = false;
	} 
	if(ok)
		printf(" %lld", n);
	else
		printf(" IMPOSSIBLE");
}

int main(){
	int T;
	scanf("%d", &T);
	for(tt =1; tt<=T; tt++){
		printf("Case #%d:",tt); // standard
		run();
		printf("\n"); // endline
	}
	return 0;
}
