/*
********************************
**      Name:Dev Bishnoi      **
**      NIT, Kurukshetra      **
**           INDIA            **
********************************
*/

#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007 
#define ll long long 
#define rep(i,a,b) for(i=a ; i<=b ; i++)
#define init(a , val ) memset(a , val , sizeof(a))// val can be possible only 0,1.
#define vi vector< int > 
#define vpii vector< pair< int , int> >
#define pii pair<int , int >
#define pi_ii pair< int , pii >
#define pii_i pair< pii, int >
#define piiii pair< pii, pii >
#define pb push_back
#define mp make_pair 
#define read(x) scanf("%d" , &x)
#define read2(x,y) scanf("%d%d",&x,&y)
#define read3(x,y,z) scanf("%d%d%d", &x, &y , &z)
#define reads(s) scanf("%s",s)
#define print(x) printf("%d\n",x)
#define print2(x,y) printf("%d %d\n",x,y)
#define fin(fname) freopen(fname,"r", stdin)
#define fout(fname) freopen(fname, "w", stdout);

int is_compatible(ll dup, int idx){
	int i = 1;
	int prev = 9;
	while(dup){
		int curr = dup % 10;
		dup = dup / 10;
		if(prev >= curr){
			prev = curr;
		}
		else
			return 0;
		i++;
	}
	return 1;
}
ll power(int m){
	int i;
	ll ans = 1;
	rep(i, 0, m-1)
		ans = ans * 10;
	return ans;
}
int main(){
	fin("B-large.in");
	fout("output.out");
	int t = 1, T;
	read(T);
	while(t <= T){
		ll n;
		cin >> n;
		ll dup = n;
		int digit = 0;
		while(dup){
			digit++;
			dup = dup / 10;
		}
		int i;
		rep(i, 1, digit){
			int flag = is_compatible(n, i);
			if(!flag){
				ll right = n / power(i);
				ll left = n % power(i-1);
				n = (right - 1) * power(i) + left + 9 * power(i-1);
			}
		}
		cout <<"Case #"<< t << ": " << n << endl;
		t++;
	}
	return 0;
}
