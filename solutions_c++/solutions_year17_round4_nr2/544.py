#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
int n, c, m, x, y, ans, ans2, T;
int A[1005], C[1005]; //seat/customer no. count.
int divi (int a, int b){
	return (a+b-1)/b;
}
ifstream inp; ofstream oup;
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(0);
	inp.open("a.in"); oup.open("a.out");
	inp>>T;
	F(t, T){
		ans = ans2 = 0;
		f(i, 1005) A[i] = C[i] = 0;
		inp>>n>>c>>m;
		f(i, m){
			inp>>x>>y;
			A[x]++;
			C[y]++;
		}
		int sum = 0;
		F(i, 1000) {
			sum+=A[i];
			ans = max(ans, divi(sum, i));
			ans = max(ans, C[i]);
		}
		F(i, 1000) if (A[i] > ans) ans2+= A[i]-ans;
		oup<<"Case #"<<t<<": "<<ans<<" "<<ans2<<endl;
		
	}
}
