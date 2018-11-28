#include<bits/stdc++.h>
using namespace std;




int main(){
	int t;
	int n;
	double d,k,s;
	float time,cur;
	cin>>t;

	for(int i=0;i<t;i++){
		cin>>d>>n;
		time=0;
		for(int j=0;j<n;j++){
			cin>>k>>s;
			cur=float((d-k)/s);
			time = max(time,cur);

		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.7f\n",float(d/time));

	}





	return 0;
}