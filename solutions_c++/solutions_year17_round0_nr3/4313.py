#include<bits/stdc++.h>
using namespace std;
string s;
int n, m, k, i, j, t;
priority_queue < pair < int , int > > q;
main(){
	   freopen("alooo.in","r",stdin);
	   freopen("alooo.out","w",stdout);
	   cin>>t;
	   for(int i=1;i<=t;i++){
			cin>>n>>k;
			while(q.size())q.pop();
			q.push(make_pair(n,1));
			for(int j=1;j<k;j++){
				int a=q.top().first;
				int b=q.top().second;
				q.pop();
			//	cout<<(a-1)/2<<" "<<b<<endl;
			//	cout<<a-(a-1)/2-1<<" "<<b+(a-1)/2+1<<endl;
			//	system("pause");
				q.push(make_pair((a-1)/2,b));
				q.push(make_pair(a-(a-1)/2-1,b+(a-1)/2+1));
			}
			cout<<"Case #"<<i<<": ";
			int a=q.top().first;
			int b=q.top().second;
			int pas1=(a-1)/2;
			int pas2=(a-(a-1)/2-1);
			cout<<max(pas1,pas2)<<" "<<min(pas1,pas2)<<endl;
	   }	   
	   }
