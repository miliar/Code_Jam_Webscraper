#include<bits/stdc++.h>
using namespace std;
int test;
int II()
{
int n;
scanf("%d",&n);
return n;
}





int main(){
	ifstream cin("C-small-2-attempt0.in");
	ofstream cout("C-small-2-attempt0.out");
cin>>test;
for(int z=1;z<=test;z++){
	long long n,k,curr=0;
	cin>>n>>k;
	priority_queue<pair<pair<long long,long long>,long long>,vector<pair<pair<long long,long long>,long long> > > stalls; 
	if(n%2==1){
		stalls.push({{n/2,n/2},1});
	}
	else{
		stalls.push({{n/2,n/2-1},1});
	}
	while(curr<k){
		pair<pair<long long,long long>,long long> temp=stalls.top();
		stalls.pop();
		if(temp.second+curr>=k){
			cout<<"Case #"<<z<<": "<<temp.first.first<<" "<<temp.first.second<<endl;
			break;
		}
		else
		curr+=temp.second;
		
		if(temp.first.first==temp.first.second){
		if(temp.first.first%2==1)
		stalls.push({{temp.first.first/2,temp.first.first/2},temp.second*2});
		else
		stalls.push({{temp.first.first/2,temp.first.first/2-1},temp.second*2});
		}
		else{
			if(max(temp.first.first,temp.first.second)%2==1){
				
				stalls.push({{max(temp.first.first,temp.first.second)/2,max(temp.first.first,temp.first.second)/2},temp.second});
				stalls.push({{min(temp.first.first,temp.first.second)/2,min(temp.first.first,temp.first.second)/2-1},temp.second});
				
			}
			else{
			stalls.push({{min(temp.first.first,temp.first.second)/2,min(temp.first.first,temp.first.second)/2},temp.second});
				stalls.push({{max(temp.first.first,temp.first.second)/2,max(temp.first.first,temp.first.second)/2-1},temp.second});	
			}
		}
		
	}
	
	
	
}
return 0;
}

