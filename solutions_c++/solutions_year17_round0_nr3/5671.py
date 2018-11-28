#include <bits/stdc++.h>
using namespace std;


int main()
{
	int t,k,n,c=1;
	cin>>t;
	ofstream out;
		out.open("file.txt");
	while(t--){
		priority_queue<int>pq;
		cin>>n>>k;
		pq.push(n);
		k--;
		while(k--){
			int a=pq.top();
			pq.pop();
			if((a-1)%2==0){
				pq.push((a-1)/2);pq.push((a-1)/2);
			}
			else{
				pq.push((a-1)/2+1);pq.push((a-1)/2);
			}
		}
		int a=pq.top();
		if((a-1)%2==0){
			out<<"Case #"<<c++<<": "<<(a-1)/2<<" "<<(a-1)/2<<"\n";
			
		}
		else out<<"Case #"<<c++<<": "<<(a-1)/2+1<<" "<<(a-1)/2<<"\n";
		
	}
}
