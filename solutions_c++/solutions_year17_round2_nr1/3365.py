#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main()
{
	int tcase;
	cin>>tcase;
	int nhorse;
	double inpo, tmpinpo, tmpspeed, tmpres;
	vector<double>inipo;
	vector<double>speed;
	double min = 200000000000000;
	for(int i = 0; i < tcase; ++i){
		cin>>inpo>>nhorse;
		//cout<<"i= "<<i<<endl;
		for(int j = 0; j < nhorse; ++j){
			cin>>tmpinpo>>tmpspeed;
			inipo.push_back(tmpinpo);
			speed.push_back(tmpspeed);
		}
		//cout<<"end vector"<<endl;
		for(int k = 0; k < inipo.size(); ++k){
			tmpres = speed[k]/(inpo-inipo[k])*inpo;
			min = min>tmpres?tmpres:min;
		}
		cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(6)<<min<<endl;
		min = 200000000000000;
		inipo.clear();
		speed.clear();
	}
	return 0;
}
