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

int a[10000];

void ft(ll n, ll k) {
	clr(a);
	ll rl = 0, rr = 0;
	ll dis = 0;
	for(int x = 0; x < k; ++x) {
		rl = 0, rr = 0;
		dis = 0;
		int t = -1;
		int o_num = 0, e_num = 0;
		for(int i = 0; i < n; ++i) {
			ll l = 0, r = 0;
			if(a[i])
				continue;
			for(int j = i-1; j >=0; --j) {
				if(a[j])
					break;
				l++;
			}
			for(int j = i+1; j<n;++j) {
				if(a[j])
					break;
				r++;
			}
			if( min(l,r) > dis ) {
				dis = min(l,r);
				rl = l;
				rr = r;
				t = i;
			}
			else if( min(l,r)==dis) {
				if(max(l,r) > max(rl,rr)) {
					dis = min(l,r);
					rl = l;
					rr = r;
					t = i;
				}
			}
			ll p = l+r;
			if(p&1)
				o_num++;
			else
				e_num++;
		}
		if(t==-1)
			break;
		//printf("n = %lld x = %d t = %d,%d l = %lld r = %lld odd num %d even num %d\n",n,x, t,a[t], rl,rr,o_num, e_num);
		a[t]=1;
	}
	cout<<max(rl,rr)<<" "<<min(rl,rr)<<endl;
}

int main()
{
	int t;
	cin>>t;
	fr(c,0,t){
		string s;
		ll n,k;
		cin>>n>>k;
		//ft(n,k);
		ll num = 1, c_o=n;
		ll o_num = 0,e_num = 0;
		if(n&1) {
			o_num = 1;
			e_num = 0;
		}
		else {
			o_num = 0;
			e_num = 1;
		}
		while(num<=k) {
			//printf("n = %lld cur = %lld num = %lld odd num %lld even num %lld\n",n, c_o, num,o_num, e_num);
			if((num<<1)-1>=k) {
				break;
			}
			num<<=1;	
			n=(n-1)/2;
			c_o=(c_o-1)/2;
			if(c_o&1) {
				o_num = (o_num<<1) + e_num;
			}
			else {
				int t = e_num;
				e_num = (o_num<<1) + e_num;
				o_num = t;
				c_o = n+1;
			}
		}
		k-=(num-1);
		ll ans = 0;
		if(n&1) {
			if(e_num>=k) {
				ans = n+1;
			}
			else {
				ans = n;
			}
		}
		else {
			if(o_num>=k) {
				ans = n + 1;
			}
			else {
				ans = n;
			}
		}
		cout<<"Case #"<<c+1<<": "<<max((ans-1)/2, ans/2)<<" "<<min((ans-1)/2,ans/2)<<endl;
	}
}
