#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>

#define ll unsigned long long int
#define MAX_DIGIT 20

using namespace std;

int ndigit;
int Number[MAX_DIGIT];
int sNumber[MAX_DIGIT];

void to_array(ll n){
	ndigit = MAX_DIGIT - 1;
	while(n != 0ll)
	{
		Number[ndigit] = (int)(n % 10ll);
		n /= 10ll;
		ndigit--;
	}
	
}

/*int vdp[MAX_DIGIT][10][2];
ll dp[MAX_DIGIT][10][2];

ll count_tidy(int k,int before,int last){
	if(k == MAX_DIGIT) return 1ll;
	
	if(vdp[k][before][last] != -1) return dp[k][before][last];
	
	vdp[k][before][last] = 1;
	dp[k][before][last] = 0ll;
	
	ll res = 0ll;
	
	int init = before;
	int fin = 9;
	
	if(last) fin = Number[k];
	
	while(init <= fin){
		int slast = 0;
		if(last && init == fin) slast = 1;
		res += count_tidy(k + 1,init,slast);
				
		init++;
	}
	
	return (dp[k][before][last] = res);	
}*/

bool flag;

void count_tidy(int k,int before,int last){
	if(k == MAX_DIGIT){
		flag = true;
		int d = ndigit + 1;
		while(sNumber[d] == 0) d++;
		for(;d < MAX_DIGIT;d++) printf("%d",sNumber[d]);
		printf("\n");
	}
	
	int fin = 9;
	
	if(last) fin = Number[k];
	int init = fin;
	
	while(init >= before && !flag){
		int slast = 0;
		if(last && init == fin) slast = 1;
		sNumber[k] = init;
		count_tidy(k + 1,init,slast);
		init--;
	}		
}

int main(){
	int t;
	ll n;
	scanf("%d",&t);
	int caso =1 ;
	while(t--){
		scanf("%lld",&n);
		to_array(n);
		flag = false;
		printf("Case #%d: ",caso++);
		count_tidy(ndigit + 1,0,1);
	}
	return 0;
}
