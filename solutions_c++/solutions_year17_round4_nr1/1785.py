/****************************
    > File Name: a.cpp
    > Author: caoyu01
  	> Mail: yalecyu@gmail.com 
    > Created Time: 2017年05月13日 星期六 22时06分43秒
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
int T,n,p,ca,a[N];
map<int,int>mp;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	cin>>T;
	for(int ca=1;ca<=T;ca++){
		cin>>n>>p;mp.clear();
		for(int i=1;i<=n;i++){
			cin>>a[i];
			a[i]%=p;
			a[i]=p-a[i];
			a[i]%=p;
		}
		sort(a+1,a+1+n);
		int now=0,ans=0;
		for(int i=1;i<=n;i++){
			if(mp[i]==1)continue;
			if(now==0)ans++;
			now+=a[i];
			now%=p;
			if(now){
				for(int j=i+1;j<=n;j++){
					if((a[j]+now)==p&&mp[j]==0){
						mp[j]=1;
						now=0;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
