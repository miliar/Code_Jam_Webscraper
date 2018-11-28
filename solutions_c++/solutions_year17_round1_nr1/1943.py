#include <bits/stdc++.h>
//#include <math.h>    work with doubles 18 significative cifras   round-mas cercano, floor-inferior, ceil-superior, trunc-truncar 
#define endl '\n'
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;
typedef long long ll ;
typedef vector<int> vi ;

int main() {
	fast_io();	
	int t,t1;
	cin>>t;
	t1=t;
	int x[4]={1,-1};
	int y[4]={0,0};
	vector<string> s;
	while(t--){
		int r,c;
		cin>>r>>c;
		s.resize(0);
		string k;
		for(int i=0;i<r;i++){
			cin>>k;
			s.push_back(k);
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(s[i][j]=='?')continue;
				else{
					for(int p=0;p<2;p++){
						if(i+y[p]>=0 && i+y[p]<r && j+x[p]>=0 && j+x[p]<c){
							if(s[i+y[p]][j+x[p]]=='?'){
								s[i+y[p]][j+x[p]]=s[i][j];
							
							}
						}
					}
				}
			}
		}
		for(int i=0;i<r;i++){
			for(int j=c-1;j>=0;j--){
				if(s[i][j]=='?')continue;
				else{
					for(int p=0;p<2;p++){
						if(i+y[p]>=0 && i+y[p]<r && j+x[p]>=0 && j+x[p]<c){
							if(s[i+y[p]][j+x[p]]=='?'){
								s[i+y[p]][j+x[p]]=s[i][j];
							
							}
						}
					}
				}
			}
		}
		vi o;
		o.resize(0);
		for(int i=0;i<r;i++){
			if(s[i][0]=='?'){
				o.push_back(i);
		//		cout<<i<<" ";
			}
		}
	//	cout<<endl;
		for(int i=0;i<o.size();i++){
			if(o[i]==0)continue;
			s[o[i]]=s[o[i]-1];
		}
		o.resize(0);
		for(int i=0;i<r;i++){
			if(s[i][0]=='?'){
				o.push_back(i);
	//			cout<<i<<" ";
			}
		}
	//	cout<<endl;
		for(int i=o.size()-1;i>=0;i--){
			if(o[i]==r-1)continue;
			s[o[i]]=s[o[i]+1];
			
		}
		cout<<"Case #"<<t1-t<<":"<<endl;
		for(int i=0;i<r;i++){
			cout<<s[i]<<endl;
		}
	}
	return 0;
}
