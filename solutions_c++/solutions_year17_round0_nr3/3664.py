/*************************************************************************
    > File Name: qua3.cpp
    > Author: Yuchen Wang
    > Mail: wyc8094@gmail.com 
    > Created Time: Sat Apr  8 15:53:10 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<utility>
#include<queue>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pi;

priority_queue<pi> process;
ll n,k;
int t;


int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	int tt = 0;
	cin >> t;
	while(t--){
		printf("Case #%d: ",++tt);
		cin >> n >> k;
		while(!process.empty())process.pop();
		process.push(make_pair(n,1));

		while(1){
			pi cur = process.top();
			process.pop();
			ll mid = (cur.first+1)/2;
			ll left = mid-1;
			ll right = cur.first - mid;
			if(k<=cur.second){
#ifdef ISTEST
				cout << cur.first << endl;
#endif
				printf("%lld %lld\n",right,left);
				break;
			}
			else{
				if(cur.first & 1)process.push(make_pair(mid-1,cur.second*2));
				else{
					process.push(make_pair(right,cur.second));
					process.push(make_pair(left,cur.second));
				}
			}
			k -= cur.second;
		}
	}
}

