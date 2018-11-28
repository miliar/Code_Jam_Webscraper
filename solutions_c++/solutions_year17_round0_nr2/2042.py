#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <functional>
#include <math.h>
#define LL long long int
#define ii pair< int,int >
#define iii pair< int , ii > 
#define vi vector<int>
#define vii vector<ii>
#define II pair< LL , LL >
#define III pair< LL  , LL > 
#define vI vector<LL>
#define rI(B) scanf("%d",&B)
#define wI(B) printf("%d",B)
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("B-large.in"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define EPS 1e-9
using namespace std;
char buffer[1000];
int main(){
	R_W;
	int t;
	cin>>t;
	int cases=1;
	while(t--)
	{
		char *ins=buffer;
		cin>>ins;
		int len=strlen(ins);
		bool Nochange=false;
		while(!Nochange){
			bool Decreased=false;
			Nochange=true;
			for(int i=0;i<len-1;i++)
			{
				if(ins[i]<=ins[i+1]) continue;
				if(!Decreased) ins[i]--,Decreased=true;
				ins[i+1]='9';
				Nochange=false;
			}
		}
		while(*ins=='0' && *(ins+1)!='\0')ins++;
		printf("Case #%d: %s\n",cases++,ins);
	}
	return 0;
}