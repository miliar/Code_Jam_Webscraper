#include<bits/stdc++.h>
using namespace std;
int hd, ad, hk, ak, b, d;
int get(int numd, int numb){
	int thd = hd;
	int tad = ad;
	int thk = hk;
	int tak = ak;
	int sum = 0;
	for(int i = 1; i <= numd; i++){
		if(max(0, tak - d) >= thd){
			sum++;
			thd = hd - tak;
			if(thd <= 0) return -1; 
		}
		sum++;
		tak = max(tak - d, 0);
		thd -= tak;
		if(thd <= 0) return -1;
	}
	for(int i = 1; i <= numb; i++){
		if(tak >= thd){
			sum++;
			thd = hd - tak;
			if(thd <= 0) return -1; 
		}
		sum++;
		tad += b;
		thd -= tak;
		if(thd <= 0) return -1;
	}
	while(1){
		if(tad >= thk) return sum + 1;
		if(tak >= thd){
			sum++;
			thd = hd - tak;
			if(thd <= 0) return -1; 
		}
		sum++;
		thk -= tad;
		thd -= tak;
		if(thd <= 0) return -1;
	}
}	
int main(){
	freopen("C_small.in", "r", stdin);
	freopen("C_small.out", "w", stdout);
	int TT;
	cin >> TT;
	for(int ii = 1; ii <= TT; ii++){
		cin>>hd>>ad>>hk>>ak>>b>>d;
		int ans = -1;
		for(int numd = 0; numd <= 110; numd++)
			for(int numb = 0; numb <= 110; numb++){
				int now = get(numd, numb);
				if(now == -1) continue;
				if(ans == -1 || now < ans) ans = now;
			}
		printf("Case #%d: ", ii);
		if(ans == -1) puts("IMPOSSIBLE");
			else cout<<ans<<endl;
	}
}
