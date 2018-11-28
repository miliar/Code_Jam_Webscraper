/* 
    Har Har Mahadev
*/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vi vector<int>
#define vll vector<long long>
#define vpii vector<pair<int,int> >
#define vpll vector<pair<long long,long long> >
#define pb(x) push_back(x)
#define mk(x,y) make_pair(x,y)
#define fir first
#define sec second
#define all(x) x.begin(),x.end()
#define frp(i,x,y) for(i=x;i<=y;i++)
#define frn(i,x,y) for(i=x;i>=y;i--)
#define mod 1000000007ll
#define FILE freopen("input.in", "rt", stdin),freopen("output.txt", "wt", stdout);


template <class T>
T expo(T x,T n) { T result=1; while(n>0){ if(n%2==1) result=(result*x)%mod; x=(x*x)%mod; n=n/2; } return result; }

// ------------------------------------------- Potha Ends Here------------------------------------------------ //

int main(){
	FILE
	int t,u=0;
	cin>>t;
	while(t--){
		u++;
		long long n,i,j,k,x,y,z,c=0;
		cin>>n>>k;
		
		priority_queue<long long> q;
		map<long long,long long> m;
		
		q.push(n);
		m[n]=1;
		c=0;
		
		while(c<k){
			 z=q.top();
			 q.pop();
			 c+=m[z];
			 if(z%2==1){
			 	 x=y=z/2;
			 }else{
			 	x=z/2-1;
			 	y=z/2;
			 }
			 if(m.find(x)!=m.end()){
			 	m[x]+=m[z];	
			 }else{
				q.push(x);
				m[x]=m[z];
			 }
			 if(m.find(y)!=m.end()){
				m[y]+=m[z];	
			 }else{
				q.push(y);
				m[y]=m[z];
			 }	
		}
		cout<<"Case #"<<u<<": "<<y<<" "<<x<<endl;
	}
}
