/* ***********************************************
Author        :axp
Created Time  :2017/4/8 23:36:27
TASK		  :B.cpp
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
int n,m;
int T;

bool ok(int n)
{
	int x=n%10;
	n/=10;
	while(n)
	{
		if(n%10>x)return 0;
		x=n%10;
		n/=10;
	}
	return 1;
}

int main()
{
    freopen("B-small-attempt0 (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
	for(int kase=1;kase<=T;kase++)
	{
		cin>>n;
		while(!(ok(n)))
			n--;
		printf("Case #%d: %d\n",kase,n);
	}
    return 0;
}
