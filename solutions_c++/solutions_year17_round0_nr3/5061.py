#include<map>
#include<iostream>
using namespace std;
int main() {
	int T, t;
	cin >> T;
	for(t=1;t<=T;t++) {
		long long N, K;
		cin >> N >> K;
		map <long long, long long> m;
		m[N]=1;
		long long a, b;
		auto beg=m.rbegin();
		while(K>0) {
			if(beg->second==0) 
//				cout<<"YAHOO!\n";
				beg++;
			long long P=beg->first;
			long long S=beg->second;
			beg->second=0;
			a=(P-1)/2;
			b=(P-1)/2;
			if(P%2==0)
				b++;
//			cout<<"a="<<a<<"b="<<b<<"\n";
			m[a]+=S;
			m[b]+=S;
//			cout<<"m[a]="<<m[a]<<"m[b]="<<m[b]<<"\n";
//			cout<<K<<"\n";
			K-=S;
		}
		cout<<"Case #"<<t<<": "<<b<<" "<<a<<"\n";
	}
}
