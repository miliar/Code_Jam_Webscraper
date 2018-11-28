#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <memory.h>
#include <sstream>
#include <deque>
const int pi=acos(-1);
typedef long long ll;
using namespace std;
const ll M=1e18;
vector<ll>v;
int j,t;
void wtf(ll z,int l)
{
	v.push_back(z);
	if(z>1e17)
		return ;
	for(int i=l;i<=9;i++)
		wtf(z*10+i,i);
}
int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	#endif
	freopen("output.txt","w",stdout);
	for(int i=1;i<=9;i++)
		wtf(i,i);
	sort(v.begin(),v.end());
	cin>>t;
	while(t--)
	{
		ll x;
		cin>>x;
		int k=upper_bound(v.begin(),v.end(),x)-v.begin();
		--k;
		cout<<"Case #"<<++j<<": "<<v[k]<<endl;
	}
	return 0;
}