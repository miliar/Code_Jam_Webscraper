/*
*	Author: Suparshva Mehta 	Username: suparsh14
*	College: DA-IICT, India
*	GCJ Round 1B
*	Q-A
*/

#include<bits/stdc++.h>

using namespace std;



int main(){

	int T;
	cin>>T;

	for(int ca=1;ca<=T;ca++)
	{
		cout<<"Case #"<<ca<<": ";

		long long D,N;
		cin>>D>>N;
		double ans=0;
		//logic starts here
		for(int i=0;i<N;i++){
			long long a,b;
			cin>>a>>b;

			double ti=1.0*(D-a)/b;
			ans=max(ans,ti);
		}

		printf("%0.8lf\n",D/ans);
	}

	return 0;
}