#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <climits>
#include <cstring>
using namespace std;

int main()
{
		
    int T;
    cin>>T;
	
    for(int t=1;t<=T;t++){
		string s;
		cin>>s;

		int n=s.size();
		long long dp[10][2]={};

		for(int i=0;i<10;i++){
			if(i<s[0]-'0')			dp[i][0]=i;
			else if(i==s[0]-'0')	dp[i][1]=i;
		}

		for(int i=1;i<n;i++){

			long long dp2[10][2]={};

			//dp[j][0]->dp2[k][0]
			for(int j=0;j<10;j++){
				for(int k=j;k<10;k++){
					dp2[k][0]=max(dp2[k][0],dp[j][0]*10LL+(long long)k);
				}
			}

			//dp[j][1]->dp2[k][0 or 1]
			for(int j=0;j<10;j++){
				for(int k=j;k<10;k++){
					if( k < s[i]-'0' ){
						dp2[k][0]=max(dp2[k][0],dp[j][1]*10LL+(long long)k);
					}else if(k==s[i]-'0'){
						dp2[k][1]=max(dp2[k][1],dp[j][1]*10LL+(long long)k);
					}
				}
			}

			for(int j=0;j<10;j++){
				memcpy(dp[j],dp2[j],sizeof(long long)*2);
			}



		}

		long long res=0;
		for(int i=0;i<10;i++){
			for(int j=0;j<2;j++) res=max(res,dp[i][j]);
		}
		printf("Case #%d: %lld\n",t,res);

	}
    
    return 0;
}