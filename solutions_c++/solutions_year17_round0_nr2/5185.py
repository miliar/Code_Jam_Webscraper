#include<bits/stdc++.h>

using namespace std;
int main(){
	fstream f,o;
	f.open("B-large.in");
	o.open("output.txt");
	int t;
	f >> t;
	int count=1;
	//cout<<t<<endl;
	for(int i=0; i<t; ++i){
		uint64_t k;
		f>> k;
		cout<<k<<endl;
		int imp=0;
		uint64_t j=k;
		while(j>0){
			
			uint64_t n=j, r=0;
			int ans=1;
			int l=1;
			
			while(n>=10){
				int d1=n%10;
				r=r*10+d1;
				n/=10;
				int d2=n%10;
				if(d2>d1){
					ans=0;
					uint64_t nm=0;
					uint64_t n10=1;
					for(int m=1; m<=l; ++m){
						nm=nm*10+9;
						n10*=10;
					}
					j=(n-1)*n10+nm;
					
					break;
				}
				++l;
			}
			cout<<j<<endl;
			if(ans==1)
				break;
		}
		o<<"Case #"<<count<<": "<<j<<"\n";
		++count;
	}
	
}