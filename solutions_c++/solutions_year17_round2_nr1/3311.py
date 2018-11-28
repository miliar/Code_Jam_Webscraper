#include"bits/stdc++.h"
using namespace std;
int main(){
	ifstream in("A-large.in.txt");
	ofstream out("output.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;++i){
		long long d;
		in>>d;
		long long x=0,y=1;
		long long n,a,b;
		in>>n;
		for(int i=0;i!=n;++i){
			in>>a>>b;
			if((d-a)*y>b*x){
				x=d-a;
				y=b;
			}
		}	
		out<<"Case #"<<i<<": "<<setprecision(15)<<(d*y)/double(x)<<endl;
	}
}
