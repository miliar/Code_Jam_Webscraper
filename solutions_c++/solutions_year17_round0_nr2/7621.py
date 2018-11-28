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
    int i,j,t;
    S(t);
    for(int tc =1;tc<=t;tc++) {
    	string str;
    	cin>>str;
    	int len = str.size();
    	int i =0;
    	while(i+1 < len && str[i] <= str[i+1]) {
    		i++;
    	}
    	int j = i;
    	if(j != len-1) {
    		// cout<<"inside before "<< str<<"\n";
    		str[j] = str[j] - 1;
    		// cout<<"inside after "<< str<<" and j char "<< str[j] <<"\n";
    	}
    	int idx = j+1;
    	// cout<<"firs " <<str<<" j====" <<j;pnl
    	int carry = 0;
    	while(j>=1) {
    		// cout<<"j=== "<<j<<" ";
    		if(str[j-1] > str[j]) {
    			idx = j;
    			// cout<<"idx=== "<<idx<<" "<<str[j-1]<<" "<<str[j]<<endl;
    			str[j-1] = str[j-1] - 1;
    			// cout<<"after idx=== "<<idx<<" "<<str[j-1]<<" "<<str[j]<<endl;
    		}
    		j--;
    	}
    	string ans = "";
    	// cout<<"j == "<<j<<endl;
    	int k = 0;
    	if(str[0] == '0') k++;
    	// cout<<"k == "<<k<<" and idx = "<<idx<<endl;
    	for(;k<=idx-1;k++) {
    		ans += str[k];
    	}
    	// cout<<ans<<endl;
    	for(;k<len;k++) {
    		ans += '9';
    	}
    	// cout<<ans<<endl;
    	printf("Case #%d: ", tc);
    	cout<< ans <<endl;
    }
return 0;
}
