#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	int t = 0;
	cin>>t;
	for(int c = 1; c <= t; c++){
		long long n = 0, k = 0;
		cin>>n>>k;
		int h = (int)log2(n);
		long long cnt = n;
		vector<long long> val(h+1, 0);
		vector<long long> s(h+1, 0);
		vector<long long> s1(h+1, 0);
		val[0] = n;
		s[0] = 1;
		for(int i = 1; i <= h; i++){
			if(val[i-1] % 2 == 0){
				val[i] = val[i-1]/2 - 1;
				s[i] += s[i-1];
				s1[i] += s[i-1] + 2*s1[i-1];
			}
			else{
				val[i] = val[i-1]/2;
				s[i] = 2*s[i-1] + s1[i-1];
				s1[i] = s1[i-1];
			}
		}
		int l = (int)log2(k);
		if(l!=0)
			k = k - (long long)pow(2,l);
		if(k < s1[l]){
			int res = val[l]+1;
			cout<<"Case #"<<c<<": "<<(res)/2<<" "<<(res - 1)/2<<endl;
		}else{
			int res = val[l];
			cout<<"Case #"<<c<<": "<<(res)/2<<" "<<(res - 1)/2<<endl;	
		}
	}
	return 0;
}