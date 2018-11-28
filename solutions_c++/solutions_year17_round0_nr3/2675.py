/*
*	Author: Suparshva Mehta 	Username: suparsh14
*	College: DA-IICT, India
*	GCJ Qualification Round
*	Q-C
*/

#include<bits/stdc++.h>

using namespace std;

void brute(long long n,long long k){	// O(K*log2(N))

	priority_queue<long long> max_pq;

	max_pq.push(n);

	long long maxi,mini;

	for(long long i=1;i<=k;i++){
		long long tp=max_pq.top();
		max_pq.pop();

		maxi=tp/2;
		mini=tp/2;

		if(tp%2==0)mini--;


		cerr<<maxi<<" "<<mini<<endl;
		max_pq.push(maxi);
		max_pq.push(mini);
	}	

	cout<<maxi<<" "<<mini<<endl;
}

void smart(long long n,long long k){	// O(log2(N))

	map< long long ,long long > max_pq;

	long long maxi,mini;

	max_pq[n]=1;

	long long i;

	for(i=1;i<=k;){

		long long tp=max_pq.rbegin()->first,counter=max_pq.rbegin()->second;
		
		max_pq.erase(tp);

		maxi=tp/2;
		mini=tp/2;
		
		i+=counter;

		if(tp%2==0){
			mini--;
		}
		max_pq[maxi]+=counter;
		max_pq[mini]+=counter;
			
	}

	cout<<maxi<<" "<<mini<<endl;

}

int main(){

	int T;
	cin>>T;

	for(int ca=1;ca<=T;ca++)
	{
		cout<<"Case #"<<ca<<": ";

		//logic starts here

		long long n,k;
		cin>>n>>k;

		//brute(n,k);
		smart(n,k);
	}

	return 0;
}