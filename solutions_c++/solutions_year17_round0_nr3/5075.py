#include <iostream>
#include <cmath>
#include <cstdio>
#define lli long long int
using namespace std;

int main(){
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
	
	int C,ic=1,ni;
	lli n, k;
	cin>>C;
	while(C--){
		cin>>n>>k;
		lli sol;
		ni= floor(log(k)/log(2));
		lli nopi = pow(2,ni);
		lli nosil = n - nopi + 1;
		lli gsa = ceil(1.0*nosil/nopi);
		lli bsa = floor(1.0*nosil/nopi);
		lli hgs = nosil - bsa*nopi;
		if(k - pow(2,ni) + 1 <= hgs){
			sol=gsa;
		}else{
			sol=bsa;
		}
		if(sol <= 1){
			cout<<"Case #"<<ic++<<": 0 0"<<endl;
		}else{
			lli sup = ceil(1.0*(sol-1)/2);
			lli inf= floor(1.0*(sol-1)/2);
			cout<<"Case #"<<ic++<<": "<<sup<<" "<<inf<<endl;
		}
	}
	return 0;
}
