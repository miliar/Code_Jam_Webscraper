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
int j;
void calc(ll x,int last)
{
	if(x>1e17)
		return ;
	v.push_back(x);
	for(int i=last;i<=9;i++)
		calc(x*10+i,i);
}
int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	#endif
	freopen("output.txt","w",stdout);
	for(int i=1;i<=9;i++)
		calc(i,i);
	sort(v.begin(),v.end());
	/*for(int i=0;i<100;i++)
		cout<<v[i]<<endl;*/
	int t;
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