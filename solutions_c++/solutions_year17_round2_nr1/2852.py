#include<iostream>
#include<vector>
#include <iomanip>
using namespace std;

int main(){
	// std::cout << std::fixed;
 //    std::cout << setprecision(2);
	std::cout << std::setprecision(6) << std::fixed;
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		double D;
		int N;
		cin>>D>>N;
		double slowest_time = -1.0;
		vector<double> start_points,speeds,times;
		for(int i=0;i<N;i++){
			double sta,spe;
			cin>>sta>>spe;
			start_points.push_back(sta);
			speeds.push_back(spe);
			double time = (D-sta)/spe;
			if(slowest_time == -1){
				slowest_time = time;
			}else{
				if(slowest_time < time){
					slowest_time = time;
				}
			}
		}
		double answer = D/slowest_time;
		cout<<answer<<endl;
	}
}