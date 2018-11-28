#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		int d,n;
		cin>>d>>n;
		int k[n],s[n];
		for(int i=0; i<n; i++){
			cin>>k[i]>>s[i];
		}
		
		double last = 0.0;
		for(int i=0; i<n; i++){
			double arr = ((double)(d - k[i]))/((double)s[i]);
			if(arr > last)
				last = arr;
		}
		
		double v = ((double)d)/last;
		
		cout<<"Case #"<<tc<<": ";
		cout.precision(10);
		cout<<fixed<<v<<endl;
	}
}