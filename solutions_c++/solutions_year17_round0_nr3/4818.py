#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll n,k;


int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>n>>k;
		
		priority_queue <ll > q;
		ll left,right;
		while(k--){
			if(n%2==0) left=n/2,right=n/2-1;
			else left=n/2,right=n/2;
			q.push(left);
			q.push(right);
			n=q.top();
			q.pop();
			}
		cout<<"Case #"<<t<<": ";
		cout<<max(left,right)<<" "<<min(left,right)<<endl;
		}
	return 0;
	}
