#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;




int main(){
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		long long n,k;
		priority_queue<int> p;
		cin>>n>>k;
		p.push(n);
		bool f=true;
		long long a,b;
		while(k--){
			long long x = p.top();
			p.pop();
			x--;
			a=x/2;
			b=x-a;
			p.push(a);
			p.push(b);
		}

		cout<<"Case #"<<j<<": "<<b<<" "<<a<<endl;
	}
}