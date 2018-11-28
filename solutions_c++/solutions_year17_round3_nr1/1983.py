#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

struct item{
public:
	int r;
	long double srf;
	bool compare(const item &lhs, const item &rhs) const
	{
	    return lhs.srf > rhs.srf;
	}
	 bool operator < (const item& str) const
	    {
		 	 if(srf==str.srf){
		 		 return r>str.r;
		 	 }
	        return (srf > str.srf);
	    }
};

long double calc(int n, int k, int*radius, int *height){
	long double surf = 0;
	vector<item> t(n);
	int vector_size = n;
	for(int i=0; i<n;i++){
		t[i].r=radius[i];
		t[i].srf=2.*(long double)radius[i]*(long double)height[i];
	}
	sort(t.begin(), t.end());

	while(vector_size>=k){
		int mr=0;
		for(int i=1;i<vector_size;i++){
			if(t[mr].r<t[i].r){
				mr=i;
			}
		}
		for(int i=0;i<vector_size;i++){
			cerr.precision(20);
			cerr<<t[i].r<<" "<<t[i].srf<<"   ";
		}
		cerr<< mr<<endl;
		long double sum = (long double)t[mr].r*(long double)t[mr].r;
		cerr<<sum<<endl;
		for(int i=0;i<k-1;i++){
			sum+=t[i].srf;
		}
		cerr<<sum<<endl;
		if(mr>k-1){
			sum+=t[mr].srf;
		}else{
			sum+=t[k-1].srf;
		}
		cerr<<sum<<endl;
		if(surf<sum){
			surf=sum;
		}
		cerr << mr <<" "<<t[mr].r<<" "<<sum <<endl;
		int rmax= t[mr].r;
		for(int i=vector_size-1;i>=0;i--){
			if(t[i].r>=rmax){
				t.erase(t.begin()+i);
				vector_size--;
			}
		}
	}

	return surf*M_PI;
}
int main(int argc,char *argv[]) {
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		cerr<<"case"<<i<<endl;
		int N, K;
		cin>>N>>K;
		int *radius= new int[N];
		int *height= new int[N];
		for(int j=0; j<N; j++){
			cin>>radius[j]>>height[j];
		}
		long double result = calc(N, K, radius, height);
		cout.precision(20);
		cout << "Case #"<< (i+1)<<": " <<result<< endl;
		delete[] radius;
		delete[] height;
	}
	return 0;
}

