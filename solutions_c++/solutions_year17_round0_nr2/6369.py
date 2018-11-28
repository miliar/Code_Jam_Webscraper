#include<iostream>
using namespace std;

int main() {
	int number_of_tests;
	cin>>number_of_tests;
	for(int test=1;test<=number_of_tests;test++) {
		string n;
		cin>>n;
		for(int i=0;i<n.size()-1;i++) {
			if(n[i]>n[i+1]) {
				for(int j=i+1;j<n.size();j++) {
					n[j]='9';
				}
				n[i]=n[i]-1;
				for(int j=i-1;j>=0;j--) {
					if(n[j]>n[j+1]) {
						n[j+1]='9';
						n[j]=n[j]-1;
					}
					else
						break;
				}
				break;
			}
		}
		if(n[0]=='0')
			n = n.substr(1,n.size());
		cout<<"Case #"<<test<<": ";
		cout<<n<<"\n";
	}
	return 0;
}
