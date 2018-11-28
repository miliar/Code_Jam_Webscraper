#include <iostream>
#include <queue>
using namespace std;

int main(){
	int t; cin>>t;
	for(int i=1;i<=t;++i){
		int n,k; cin>>n>>k;
		priority_queue<int> q;		
		q.push(n);
		int mi, ma;
		while(k--){
			int x=q.top();
			q.pop();
			x--;
			mi=x/2;
			ma=x-mi;
			q.push(ma);
			q.push(mi);
		}
		cout<<"Case #"<<i<<": "<<ma<<" "<<mi<<endl;
	}
	return 0;
}
