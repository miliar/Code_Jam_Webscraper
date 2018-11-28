#include<bits/stdc++.h>
using namespace std;
#include<limits>
#define f(k, n) for(int ii=k; ii<=n; ii++)
#define fz(t, n) for(int jj=t; jj<=n; jj++)
#define inf(type) numeric_limits<type>::max()
#define infinity INT_MAX
#define reset(v) memset(v, 0, sizeof(v)) 
#define arraysize(v) (sizeof v)/(sizeof v[0])
#define setarray(v, k) fill(v, v+arraysize(v), k)
int main(){
	freopen("A-large.in", "r", stdin);
    freopen("out1.out", "w", stdout);
    int T, temp;
	cin>>T;
	fz(1, T){
	 long double D, N, maxDis=0, maxSpd=0, maxTime=0, dis, spd, time;
	 cin>>D>>N;
	 for(int i=1; i<=N; i++){
	 	cin>>dis>>spd;
	 	time=(D-dis)/spd;
	 
	 	if(time>maxTime){
	 		
	 		maxTime=time;
		 }
		 
	 }
	 maxSpd=D*1.000000/maxTime;
	 //maxSpd*=1.000000;
	 cout.precision(20);
		cout<<"Case #"<<jj<<": "<<maxSpd<<endl;
	}

	

	return 0;
}
