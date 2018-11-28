/****************************
    > File Name: a.cpp
    > Author: caoyu01
  	> Mail: yalecyu@gmail.com 
    > Created Time: 2017年04月23日 星期日 00时08分23秒
*****************************/
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define cle(x) memset(x,0,sizeof(x))
#define rep(i,x) for(int i=0;i<x;i++)
#define Rep(i,x) for(int i=1;i<=x;i++)
const int N = 1000+10;
const int mod = 1e9+7;
const int inf = 0x3f3f3f3f;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);
#endif
	int T;
	cin>>T;
	int ca=1;
	while(T--){
		int k,d,n,m;
		cin>>d>>n;
		double mx=0;
		while(n--){
			cin>>k>>m;
			mx=max(mx,1.0*(d-k)/(1.0*m));
		}
		printf("Case #%d: %.10lf\n",ca++,d/mx);
	}
	return 0;
}
