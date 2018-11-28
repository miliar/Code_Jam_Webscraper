#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		long long int n,k;
		cin>>n;
		cin>>k;
		priority_queue<long long int> q;
		q.push(n);
		long long int i=0,x,y;
		while(!q.empty()&&i<k){
			long long int m=q.top();
			q.pop();
			if(m%2==0){
				x=m/2;
				y=x-1;
			}
			else{
				x=m/2;
				y=x;
			}
			q.push(y);
			q.push(x);
			i++;
		}
		cout<<"Case #"<<j<<": ";
		cout<<x<<" "<<y<<endl;

	}
	return 0;
}