#include<bits/stdc++.h>
#define mpr make_pair
#define ff first
#define ss second
#define pb push_back
#define ll long long 
using namespace std;

typedef priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >, std::greater<pair<int,pair<int,int> > > > PQ;

//scanf ("%[^\n]%*c",inp);

int main(){
	
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	
	
	int te,t=1;
	scanf("%d\n",&te);
	
	while(t<=te){
		
		
		
	int N,K;
	cin>>N>>K;
	priority_queue<int,vector<int>> Q;
	Q.push(N);
	while(--K){
	
	int curr=Q.top();
	Q.pop();
	int l=curr/2;
	int r=(curr-1)/2;
	
	if(l!=0)
	Q.push(l);
	if(r!=0)
	Q.push(r);		
		
		
	}
		
	int curr=Q.top();
	Q.pop();
	
	int l=curr/2;
	int r=(curr-1)/2;		
	cout<<"Case #"<<t<<": "<<l<<" "<<r<<endl;
	t++;
	}

return 0;	
}

