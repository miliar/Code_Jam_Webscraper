#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

vector <int> a;
void parser(ll bil) {
	ll temp = bil;
	while(temp>0) {
		int angka = temp%10;
		a.push_back(angka);
		temp/=10;
	}
	reverse(a.begin(), a.end());
}

bool isSorted() {
	int i;
	int n = a.size();
	/*printf("array:");
	for(i = 0; i < n; i++) {
		printf(" %d",a[i]);
	}*/

	bool found = true;
	for(i = 0; i < n-1; i++) {
		if(a[i] > a[i+1]) {found = false; break;}
	}
	return found;
}


int main() {
	int tc,test=1;
	ll n, hi, lo, mid, ans;
	bool found;
	scanf("%d",&tc);
	while(tc--) {
		printf("Case #%d: ",test++);
		scanf("%lld",&n);
		//printf("n : %lld\n",n);
		//cari bil itu
		
		
		/*if(!found){
			hi = n, lo = 0;
			while(lo < hi) {
				a.clear();
				mid = (hi+lo)/2;
				printf("hi: %lld lo: %lld mid: %lld\n",hi,lo,mid);
				parser(mid);
				if(isSorted()){lo = mid+1;}
				else{
					hi = mid;
				}
			}
			if(lo > n) {lo = n;}
			a.clear();
			parser(lo);
			if(isSorted()){ans = lo;}
			else{ans = hi;}
		}*/
		ll bil = n;
		found = false;
		while(!found) {
			//printf("bil : %lld\n",bil);
			a.clear();
			parser(bil);
			if(isSorted()) {found = true; ans = bil;}
			else{bil--;}
		}
		cout<<ans<<endl;
	}
	return 0;
}
