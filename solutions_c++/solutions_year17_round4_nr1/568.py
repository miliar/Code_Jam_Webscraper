#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
int T, ans;
int n, A[4], x, p;
ifstream inp; ofstream oup;
void printans(int t, int x){
	oup<<"Case #"<<t<<": "<<x<<endl;
}
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(0);
	inp.open("a.in"); oup.open("a.out");
	inp>>T;
	F(t, T){
		f(i, 4) A[i] = 0;
		ans = 0;
		inp>>n>>p;
		f(i, n){
			inp>>x;
			A[x%p]++;
		}
		ans = A[0];
		A[0] = 0;
		F(i, p-1) if (A[i]>0 && A[p-i]>0) {if (i*2!=p){
			x=min(A[i], A[p-i]);
			A[i]-= x;
			A[p-i]-=x;
			ans +=x;
		}
		else{
			ans += A[i]/2;
			A[i] %= 2;
		}}
		if (p==2) printans(t, ans+(A[1]>0));
		if (p==3) {
			F(i, 2) {ans += A[i]/3; A[i] %=3;}
			printans(t, ans+(A[1]+A[2]>0));
		}
		if (p==4){
			if (A[2]>0){
				if (A[1]>=2) {
					A[1]-=2;
					A[2]--;
					ans++;
				}
				else if (A[3]>=2) {
					A[3]-=2;
					A[2]--;
					ans++;
				}
			}
			F(i, 3) {ans+=A[i]/4; A[i]%=4;}
			printans(t, ans+(A[1]+A[2]+A[3]>0));
		}
	}
}
