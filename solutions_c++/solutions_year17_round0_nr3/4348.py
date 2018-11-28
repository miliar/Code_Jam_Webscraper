#include<bits/stdc++.h>
using namespace std;
int calculate_answer(int n, int k){
	priority_queue < int > pq;
	pq.push(n);
	for(int i=1;i<k;i++){
		int t = pq.top();
		pq.pop();
		pq.push(t/2);
		pq.push((t-1)/2);
	}
	return pq.top();
}
int main(){
	ifstream in("input.in");
	ofstream out("output.out");
	int t;
	in>>t;
	for(int i=1; i<=t;i++){
		int n, k;
		in>>n>>k;
		int ans = calculate_answer(n, k);
		out<<"Case #"<<i<<": "<<ans/2<<" "<<(ans-1)/2<<endl;	
	}
	return 0;
}