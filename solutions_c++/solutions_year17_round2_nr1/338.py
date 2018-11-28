#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
double guess;
int n, T;
double D;
double x, y, tim;
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(0);
	ifstream inp;
	ofstream oup;
	inp.open("a.in");
	oup.open("a.out");
	oup<<setprecision(9)<<fixed;
	inp>>T;
	F(t, T){
		tim = 0;
		inp>>D>>n;
		f(i, n){
			inp>>x>>y;
			tim = max(tim, (D-x)/y);
		}
		oup<<"Case #"<<t<<": "<<D/tim<<endl;
	}
}

