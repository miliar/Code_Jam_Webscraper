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

int main()
{
	int t;
	cin>>t;
	fr(c,0,t){
		string s;
		int k;
		cin>>s;
		cin>>k;
		int ans = 0;
		fr(i,0,s.size()) {
			if(s[i] == '-') {
				if(i+k>s.size()) {
					ans = -1;
					break;
				}
				fr(j,0,k) {
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
				++ans;
			}
		}
		if(ans>=0)
			printf("Case #%d: %d\n",c+1,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",c+1);

	}
}
