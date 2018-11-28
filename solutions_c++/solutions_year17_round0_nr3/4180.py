#include <bits/stdc++.h>

using namespace std;

priority_queue<long int> q;

void insert(){
	long int i = q.top()-1;
	long int l = i/2;
	long int r = i/2;
	if(i%2!=0){
		r = r+1;
	}
	q.pop();
	q.push(l);
	q.push(r);
}

int main(){
	int t;
	long int n,k;
	cin>>t;

	for(int i=0;i<t;i++){
		cin>>n;
		cin>>k;
		q = priority_queue <long int>();
		q.push(n);
		for(int j=0;j<k-1;j++){
			insert();
		}
		long int x = q.top()-1;
		long int l = x/2;
		long int r = x/2;
		if(x+1!=0 && x%2!=0){
			r = r+1;
		}
		cout<<"Case #"<<i+1<<": "<<r<<" "<<l<<endl;
	}



}