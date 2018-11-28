#include <bits/stdc++.h>
using namespace std;

int main()
{
	int a,d,n,m[1010],s[1010],f,b=1;
	double l,r,mid;
	cin>>a;
	while(a--){
		cin>>d>>n;
		for(int q=0;q<n;++q)cin>>m[q]>>s[q];
		l=0;
		r=DBL_MAX;
		for(int i=0;i<1000000;++i){
			mid=(l+r)/2;
			f=0;
			for(int q=0;q<n;++q)
				if(double(d-m[q])/s[q]>double(d)/mid){
					f=1;
					break;
				}
			if(f)r=mid;
			else l=mid;
		}
		cout<<"Case #"<<b++<<": ";
		cout<<fixed<<setprecision(6)<<l<<endl;
	}
	return 0;
}

