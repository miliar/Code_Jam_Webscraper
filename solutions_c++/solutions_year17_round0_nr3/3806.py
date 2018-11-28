#include <bits/stdc++.h>
using namespace std;
int main(){
	ifstream fin("D:/C++/C-small-2-attempt0.in");
	ofstream fout("D:/C++/C-small-2-attempt0.out");
	long long t,k,n,j,small,large;
	fin>>t;
	for ( int i = 0 ; i<t ; i++){
		fin>>n>>k;
		j=1;
		while ((1<<j) -1 <k){
			j++;
		}
		j--;
		if (k==1){
			fout<<"Case #"<<i+1<<": "<<n/2<<' '<<(n-1)/2<<endl;
		} else{
			small = (n-((1<<j) -1))/(1<<j);
			large = (n-((1<<j) -1)) - (small*(1<<j));
			if (k-((1<<j) -1)<=large){
				fout<<"Case #"<<i+1<<": "<<(small+1)/2<<' '<<small/2<<endl;
			} else{
				fout<<"Case #"<<i+1<<": "<<small/2<<' '<<(small-1)/2<<endl;
			}
		}
	}
}
