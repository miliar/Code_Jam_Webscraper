#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int divup(int a, int b){
	int res = a/b;
	if(a%b!=0)
		res++;
	return res;
}

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		int n,c,m;
		cin>>n>>c>>m;

		int seat[n+1];
		int cust[c+1];
		for(int i=1; i<=n; i++){
			seat[i] = 0;
		}
		for(int i=1; i<=c; i++){
			cust[i] = 0;
		}
		
		int p[m],b[m];
		for(int i=0; i<m; i++){
			cin>>p[i]>>b[i];
			seat[ p[i] ]++;
			cust[ b[i] ]++;
		}
		
		int maxCust = 0;
		for(int i=1; i<=c; i++)
			maxCust = max(maxCust, cust[i]);
		
		int maxSeat = 0;
		int sumup = 0;
		for(int i=1; i<=n; i++){
			sumup += seat[i];
			maxSeat = max(maxSeat, divup(sumup,i) );
		}
		
		int rides = max(maxCust, maxSeat);
		int prom = 0;
		for(int i=1; i<=n; i++){
			prom += max(0,seat[i]-rides);
		}
		
		cout<<"Case #"<<tc<<": "<<rides<<" "<<prom<<endl;
	}
}