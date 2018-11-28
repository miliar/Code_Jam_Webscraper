#include<iostream>
#include<string>
#include<math.h>
#include <bits/stdc++.h>

using namespace std;
int main(){
	int t,k,bits, i=0;
	string a = "---+-++-";
	cin>>t;
	while(i<t)
	{
		i++;
		cout<<"Case #"<<i<<": ";
		cin>>a;
		bits = a.size();
		for(int i = 0; i<bits;i++){
			if(a[i] == '-')
				a[i] = '0';
			else
				a[i] = '1';
		}
		cin>>k;
		bitset<1000> b(a);
		int count = 0;
		for(int i=0; i<bits-k+1;i++){	
			if(b[i]==0){
				for(int j=0;j<k;j++)
					b[i+j] = ~b[i+j];
				count++;
			}
		}
		if(b.count() == bits)
			cout<<count<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
		}
	return 0;
}
