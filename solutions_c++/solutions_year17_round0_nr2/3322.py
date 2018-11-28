#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>

#include <math.h>
#include <set>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long
#define ull unsigned long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;

ll dp[20][20][2];
int a[20];

struct Node {
	ll t;
	int flag;
	int num;
	Node(){

	}
	Node(ll t, int flag, int num) : t(t), flag(flag),num(num) {}
};
int main()
{
	int t;
	cin>>t;
	fr(c,0,t){
		string s;
		cin>>s;
		fr(i,0,s.size()){
			a[i] = s[i]-'0';
		}
		clr(dp);

		fr(i,1,a[0]) {
			dp[0][i][0]=i;
		}

		int n = s.size();
		dp[0][a[0]][1]=a[0];

		fr(i,1,n) {
			fr(j,1,10) {
				fr(k,1,j+1) {
					dp[i][j][0]=max(dp[i][j][0],dp[i-1][k][0]*10+j);
				}
				if(j<a[i]&&j>=a[i-1]) {
					dp[i][j][0]=max(dp[i][j][0],dp[i-1][a[i-1]][1]*10+j);
				}
			}
			if(a[i]>=a[i-1])
				dp[i][a[i]][1]=max(dp[i][a[i]][1], dp[i-1][a[i-1]][1] * 10 + a[i]);
		}
		
		long long ans = 0;
		for(int i = 0; i < n; ++i) {
			for(int j = 1; j < 10; ++j) {
				ans = max(ans, dp[i][j][0]);
				ans = max(ans, dp[i][j][1]);
			}
		}

		cout<<"Case #"<<c+1<<": "<<ans<<endl;
	}
}
