#include <iostream>
using namespace std;

long tidyNumber(long m){
	int units,tens;
	for(long i=m;i>0;i--){
		int x=i;
		bool value=false;
		while(x>0){
			long y=x;
			units=x%10;
			y=y/10;
			tens=y%10;
			if((units-tens)>=0){
				value=true;
				x=x/10;
				continue;
			}
			else{
				value=false;
				break;
			}
		}
		if(value)
			return i;
	}
}

int main() {
	int t,count=1;
	long n;
	cin>>t;
	while(t--){
		cin>>n;
		cout<<"Case #"<<count<<": "<<tidyNumber(n)<<endl;
		count++;
	}
	return 0;
}