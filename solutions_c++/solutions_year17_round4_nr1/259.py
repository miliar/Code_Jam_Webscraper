#include <bits/stdc++.h>

using namespace std;

#define pb push_back
typedef long long LL;
int n,p;
int a[110];

void solve2(){
	int res = 0;
	int odd = 0;
	for(int i=0; i<n; i++){
		cin >> a[i];
		if(a[i]&1){
			odd++;
		}else{
			res++;
		}
	}
	res += odd/2;
	if(odd&1) res++;
	cout << res << endl;
}

void solve3(){
	int res = 0;
	int r1=0,r2=0;
	for(int i=0; i<n; i++){
		cin >> a[i];
		if(a[i]%3==0){
			res++;
		}else if(a[i]%3==1){
			r1++;		
		}else{
			r2++;
		}
	}
	int mn = min(r1,r2);
	int mx = max(r1,r2);
	res += mn;
	mx-=mn;
	res += mx/3;
	if(mx%3) res++;
	cout << res << endl;
}

void solve4(){
	int res = 0;
	int r1=0, r2=0, r3=0;
	for(int i=0; i<n; i++){
		cin >> a[i];
		if(a[i]%4==0){
			res++;
		}else if(a[i]%4==1){
			r1++;		
		}else if(a[i]%4==2){
			r2++;
		}else{
			r3++;
		}
	}
	int mn = min(r1,r3);
	int mx = max(r1,r3);
	res += mn;
	mx-=mn;
	res += r2/2;
	r2 %=2;
	if(r2 && mx >= 2){
		res++;
		mx-=2;
	}
	if(mx){
		res += mx/4;
		if( mx%4) res++;
	}
	cout << res << endl;
}




void solve(int test){
	cout << "Case #" << test + 1 << ": ";
	cin >> n >> p;
	if(p==2){
		solve2();		
	}else if(p==3){
		solve3();
	}else{
		solve4();
	}
}
	


int ntest;
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	//freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
