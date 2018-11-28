#include<bits/stdc++.h>
#include <cstdio>
using namespace std;

typedef long long ll;

template<typename T>
void display(T first, T last){
	while(first!=last){cout<<*first++;}cout<<"\n";
}

int main(){
	fstream f,o;
	f.open("A-large.in");
	o.open("output.txt");
	ll t;
	f >> t;
	ll count=1;
	ll k;
	ll d,n;
	while(f>>d>>n){
		ll k;
		ll s;
		vector<double> time(n);
		for(int i=0; i<n; ++i){
			f>>k>>s;
			time[i] = (double)(d-k)/s;
		}
		display(time.begin(), time.end());
		double ann= *max_element(time.begin(), time.end());
		cout<<ann<<endl;
		
		o<<"Case #"<<count<<": ";
		o<<std::fixed << std::setprecision (6)<< (d/ann)<<"\n";

		++count;
	}
	
}