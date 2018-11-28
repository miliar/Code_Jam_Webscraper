#include <iostream>
#include <iomanip>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int t;
	cin>>t;
	for (int g=1;g<=t;g++){
		double k,d,n,m;
		double res=0;
		cin>>d>>n;
		for (int i=0;i<n;i++){
			cin>>k>>m;
			if ((d-k)/m>res) res=(d-k)/m;
		}
		cout<<"Case #"<<g<<": ";
		cout<<fixed<<setprecision(6)<<d/res<<endl;
	}
	return 0;
}
