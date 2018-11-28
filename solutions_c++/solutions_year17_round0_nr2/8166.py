#include<bits/stdc++.h>
#define lli long long int

using namespace std;

int xx=0,q;
lli nums[4686850],p[20],v;
		 
void f(int pos,int last,lli n){
	if(pos==19) return;
	if(n!=0) nums[xx++]=n;

	for(int i=last;i>=1;i--)
		f(pos+1,i,n+i*p[pos]);
}

int main(){

	cin.sync_with_stdio(0); cin.tie(0);

	p[0]=1;
	for(int i=1;i<=19;i++)
		p[i]=10*p[i-1];

	f(0,9,0);
	sort(nums,nums+xx);

	cin>>q;

	for(int i=1;i<=q;i++){
		cin>>v;
		int aux=upper_bound(nums,nums+xx,v)-nums;
		cout<<"Case #"<<i<<": "<<nums[aux-1]<<"\n";
	}


	return 0;
}