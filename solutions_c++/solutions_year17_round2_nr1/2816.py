#include<bits/stdc++.h>
#define FOR(a,b,c) for(a=b;a<c;a++)
#define PI acos(-1)
using namespace std;
int tc,t,i,j,n,k,d,a,b;
double hasil;
int main()
{
	cin >> tc;
	FOR(t,1,tc+1){
		printf("Case #%d: ",t);
		cin >> d >> n;
		hasil = -1;
		
		FOR(i,0,n){
			cin >> a >> b;
			hasil = max (hasil, (d - a)*1.0/(b*1.0));
		}
		printf("%.6lf\n",d*1.0/(hasil));
	}
}

