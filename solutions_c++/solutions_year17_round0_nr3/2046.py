/*ckpeteryu Code Jam 2017 QR - Problem C Bathroom Stalls*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int

int nt;
LL N,K;

LL findMin(LL n,LL k){
	LL c=k,d=1;
	while(c>0){
		c-=d;
		d*=2;
	}
	LL ret=(n-k)/d;
	return ret;
}

LL findMax(LL n,LL k){
	LL c=k,d=1;
	while(c>0){
		c-=d;
		d*=2;
	}
	LL ret=(n-k+d/2)/d;
	return ret;
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	scanf("%d",&nt);
	FOE(k,1,nt){
		scanf("%lld%lld",&N,&K);		
		printf("Case #%d: %lld %lld\n",k,findMax(N,K),findMin(N,K));
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}