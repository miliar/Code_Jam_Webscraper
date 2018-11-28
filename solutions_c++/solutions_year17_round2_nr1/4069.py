#include<iostream>
#include<iomanip>
using namespace std;
int main(){
	long long int t,num=0;
	cin>>t;
	while(t--){
		num++;
		long long int n;
		double d;
		cin>>d>>n;
		double arr[n][2];
		for(long long int i=0;i<n;i++){
			cin>>arr[i][0]>>arr[i][1];
		}
		cout<<"Case #"<<num<<": ";
		if(n==2){
			if(arr[0][0] > arr[1][0]){
				double temp1, temp2;
				temp1 = arr[0][0];
				temp2 = arr[0][1];
				arr[0][0]=arr[1][0];
				arr[0][1]=arr[1][1];
				arr[1][0]=temp1;
				arr[1][1]=temp2;
			}
			double t1=0,dist=0,t2=0;
			t1= (arr[1][0] - arr[0][0])/(arr[0][1] - arr[1][1]);
			if(t1>0){
				dist= arr[0][1]*t1+arr[0][0];
			} else dist = d+1;
			if(dist > d) {
				t1 = (d - arr[0][0])/arr[0][1];
				t2= 0;
			}
			else{
				t2 = (d - arr[1][0])/arr[1][1];
			}
			double ans;
			if(t2==0)
			ans=(arr[0][1] + (arr[0][0])/t1);
	 		else ans= (arr[1][0])/(t2) + arr[1][1];
	 		cout << fixed;
    		cout << setprecision(6);
			cout<<ans;
		}
		else if(n==1){
			double t;
			t = (d - arr[0][0])/arr[0][1];
			double ans;
			ans=(arr[0][1] + (arr[0][0])/t);
	 		cout << fixed;
    		cout << setprecision(6);
			cout<<ans;
		}
		cout<<"\n";
	}
}