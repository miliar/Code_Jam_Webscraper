#include<bits/stdc++.h>
using namespace std;

bool compare(pair<char,int> a,pair<char,int> b){
	return a.second>b.second;
}

int main(){
	int n,r,o,y,g,b,v,i,t;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>n>>r>>o>>y>>g>>b>>v;
		if(r<=(n/2) && y<=(n/2) && b<=(n/2)){
			vector<char> a(n+1);
			vector< pair<char,int> > V(3);
			pair<char,int> p;
			p.first='R';
			p.second=r;
			V[0]=p;
			p.first='Y';
			p.second=y;
			V[1]=p;
			p.first='B';
			p.second=b;
			V[2]=p;
			sort(V.begin(),V.end(),compare);
			int k,j=0;
			for(k=1;k<=n && V[j].second>0;k=k+2){
				a[k]=V[j].first;
				V[j].second--;
			}
			j++;
			for(;k<=n && V[j].second>0;k=k+2){
				a[k]=V[j].first;
				V[j].second--;	
			}
			for(k=2;k<=n && V[j].second>0;k=k+2){
				a[k]=V[j].first;
				V[j].second--;	
			}
			j++;
			for(;k<=n && V[j].second>0;k=k+2){
				a[k]=V[j].first;
				V[j].second--;	
			}
			cout<<"Case #"<<i<<": ";
			for(k=1;k<=n;k++){
				cout<<a[k];
			}	
			cout<<endl;
		}
		else	cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}