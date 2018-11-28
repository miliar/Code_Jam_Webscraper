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

int main(){
	fin("C-large.in");
	fout("output.out");
	int t = 1, T;
	read(T);
	while(t <= T){
		ll n, k;
		cin >> n >> k;
		map< ll, ll > slot;
		slot[n] = 1;
		map< ll, ll > :: iterator it;
		ll mn, mx;
		while(k>0){
			it = slot.end();
			it--; // now pointing to last element;
			ll size = it->first;
			ll cnt = it->second;
			ll curr = k;
			if(cnt < curr )
				curr = cnt;
			k = k - curr;
			ll left = (size - 1) / 2;
			ll right = size/2;
			if(cnt == curr){
				slot.erase(it);
			}
			if(k == 0){
				mn = min(left, right);
				mx = max(left, right);
				break;
			}
			if(left)
				slot[left] += curr;
			if(right)
				slot[right] += curr;
		}
		cout << "Case #"<< t << ": " << mx <<" "<< mn << endl;
		t++;
	}
	return 0;
}
