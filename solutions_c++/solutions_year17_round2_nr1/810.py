
#include <iostream>
#include <iomanip>
using namespace std;
typedef long long ll;

int no_cases;

int main(){
	cin>>no_cases;
	cout<<fixed<<setprecision(8);
	for (int caseID=1; caseID<=no_cases; caseID++){
		ll k, s, d, n;
		cin>>d>>n;
		double rt=-1;
		for (int i=0; i<n; i++){
			cin>>k>>s;
			double speed= 1.0*(d*s)/(d-k);

			if (rt==-1 || rt>speed)
				rt=speed;
		}
		cout<<"Case #"<<caseID<<": "<<rt<<endl;
	}
}
