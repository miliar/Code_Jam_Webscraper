//	Mohib Manva
#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
#define LOCAL 1
#define pb push_back
#define ll long long

ll po(ll a,ll b){
	ll x = 1,y=a;
	while(b>0){
		if(b%2){
			x = x*y;
			x %= mod;
		}
		y=y*y;
		y%=mod;
		b/=2;
	}
	return x;
}

class cmp{
public:
	bool operator() (pair<int,int> a,pair<int,int> b){
		int mi = (a.second+a.first)>>1;
		int mi1 = (b.second+b.first)>>1;
		int ls1 = mi - a.first;
		int lr1 = a.second - mi;
		int ls2 = mi1 - b.first;
		int lr2 = b.second - mi1;
		int _mi = min(ls1,lr1);
		int _ma = max(ls1,lr1);
		int _mi1 = min(ls2,lr2);
		int _ma1 = max(ls2,lr2);
		if(_mi!=_mi1){
			return (_mi<_mi1);
		}
		if(_ma!=_ma1){
			return (_ma<_ma1);
		}
		return (a>b);
	}
};

int main(){
	if(LOCAL){
    	freopen("C-small-2-attempt0.in","r",stdin);
    	freopen("output.txt","w",stdout);
	}
	int t = 1;
	int T = 1;
	scanf("%d",&T);
	while(T--){
		priority_queue<pair<int,int>,vector<pair<int,int> >,cmp> q;
		int n,k;
		scanf("%d %d",&n,&k);
		q.push(make_pair(1,n));
		printf("Case #%d: ",t++);
		pair<int,int> a;
		while(k--){
			pair<int,int> tmp = q.top();
			q.pop();
			a = tmp;
			int mi = (tmp.first+tmp.second)>>1;
			//printf("mi :%d\n",mi);
			if(tmp.first!=mi){
				q.push(make_pair(tmp.first,mi-1));
			}
			if(mi!=tmp.second){
				q.push(make_pair(mi+1,tmp.second));
			}
		}
		//printf("ANS:%d %d\n",a.first,a.second);
		int mi = (a.second+a.first)>>1;
		int ls1 = mi - a.first;
		int lr1 = a.second - mi;
		int _mi = min(ls1,lr1);
		int _ma = max(ls1,lr1);
		printf("%d %d\n",_ma,_mi);
	}
	return 0;	
}