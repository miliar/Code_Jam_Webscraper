#define MOD 1000000007
#define P printf(" yes ")
#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,j;
	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);
	cin>>t;
	for(j=1;j<=t;j++){
		long long int n,k,i,a;
		cin>>n>>k;
		priority_queue<long long int>q;
		q.push(n);
		for(i=1;i<=k;i++){
			a=q.top();
			q.pop();
			q.push(a/2);
			q.push((a-1)/2);
			if(i==k){
				cout<<"Case #"<<j<<": "<<max(a/2,(a-1)/2)<<" ";
				cout<<min(a/2,(a-1)/2)<<endl;
			}
		}
	}
	
}

