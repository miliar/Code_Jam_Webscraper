/* ***********************************************
Author        :axp
Created Time  :2017/4/8 22:50:28
TASK		  :C.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef long long ll;
const int inf = 1<<30;
const int md = 1e9+7;
ll n,k;
int T;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%lld%lld",&n,&k);
		while(k!=1)
		{
			if(k&1)
			{
				n=(n-1)/2;
				k=(k-1)/2;
			}
			else
			{
				n=n/2;
				k/=2;
			}
		}
		ll a2=(n-1)/2;
		ll a1=(n-1)-a2;
		printf("Case #%d: %lld %lld\n",kase,a1,a2);
	}
    return 0;
}
