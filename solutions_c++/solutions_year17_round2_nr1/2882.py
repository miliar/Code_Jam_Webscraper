#include<iostream>
#include<vector>

using namespace std;
int main(){
	int t;
	cin>>t;
	for(int k = 1;k<=t;k++){
		long int n;
		int d;
		cin>>n>>d;
		vector<double> arr;
		for(int i = 0;i<d;i++){
			long int pos,speed;
			cin>>pos>>speed;
			double temp = (double)(n - pos)/speed;
			arr.push_back(temp);  
		}
		double max = arr[0];
		for(int i = 1;i<d;i++){
			if(max<arr[i]){
				max = arr[i];
			}
		}
		double res = 0.0;
		res = (double)n/max;
		cout<<"Case #"<<k<<": ";
		printf("%.6lf",res);
		cout<<endl;
	}
}
