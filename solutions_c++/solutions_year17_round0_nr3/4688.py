#include <bits/stdc++.h>
#define ulli unsigned long long int
using namespace std;

int main(){
	int t;
	cin>>t;
	for (int cs=1; cs<=t; cs++){
		cout<<"Case #"<<cs<<": ";

		ulli n, k;
		cin>>n>>k;
		priority_queue<ulli> arr;
		arr.push(n);
		ulli temp;
		temp = n;
		for (int i=0; i<k-1; i++){
			temp = arr.top();
			arr.pop();
			if (temp%2){
				arr.push(temp/2);
				arr.push(temp/2);
			} else {
				arr.push(temp/2);
				arr.push((temp/2)-1);
			}
		}
		temp = arr.top();
		if (temp%2){
			cout<<temp/2<<" "<<temp/2;
		} else {
			cout<<temp/2<<" "<<((temp/2)-1);
		}

		cout<<endl;
	}
	return 0;
}