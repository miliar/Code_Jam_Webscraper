#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<climits>
#include<map>
#include<math.h>
#include<algorithm>
#define LL long long int
#define P(N) printf("%d\n",N);
#define S(N) scanf("%d",&N);
#define SL(N) scanf("%lld",&N);
#define pb push_back
#define mp make_pair
#define pnl printf("\n");
#define FOR(i,a,b) for (i=a;i<=b;i++)
#define mem(a,val) memset(a,val,sizeof(a))
using namespace std;
int gcd(int a, int b){ int temp; while(b>0) { temp= b; b=a%b; a=temp;}  return a;}
int main()
{
    int i,j,t,K;
    S(t);
    string str;
    for(int tc=1;tc<=t;tc++){
    	cin>>str>>K;
    	int count = 0;
    	int len = str.size();
    	for(int i=0;i+K <=len;i++) {
    		if(str[i]=='-') {
    			for(int j=i;j<i+K;j++) {
  					str[j] = (str[j] == '-') ? '+' : '-';
    			}
    			count++;
    		}
    	}
    	bool ans = true;
    	for(int i=0;i<len;i++) {
    		if(str[i] !='+') {
    			ans = false;
    			break;
    		}
    	}
    	printf("Case #%d: ", tc);
    	if(ans) {
    		cout<<count;
    	} else {
    		cout<<"IMPOSSIBLE";
    	}
    	pnl
    }
return 0;
}
