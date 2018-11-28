#include<iostream>
using namespace std;
int main(){
	int t,n,man=0,r,o,y,g,b,v,x;
	cin>>t;
	while(t--){
	man++;
			cin>>n>>r>>o>>y>>g>>b>>v;
			cout<<"Case #"<<man<<": ";
		x=max(max(r,y),b);
		if(x==r){
			if(x>y+b){
				cout<<"IMPOSSIBLE";			
			}
			else {
				while(x!=(y+b)){
					if(y>b){
						cout<<"R"<<"Y"<<"B";
					}
					else{
						cout<<"R"<<"B"<<"Y";
					}
					y--;
					b--;
					x--;
				}
				while(y!=0){
					cout<<"R"<<"Y";
					y--;
				}
				while(b!=0){
					cout<<"R"<<"B";
					b--;
				}
			}
		}
		else if(x==y){
			if(x>r+b){
				cout<<"IMPOSSIBLE";			
			}
			else {
				while(x!=(r+b)){
					if(r>b){
						cout<<"Y"<<"R"<<"B";
					}
					else{
						cout<<"Y"<<"B"<<"R";
					}
					r--;
					b--;
					x--;
				}
				while(r!=0){
					cout<<"Y"<<"R";
					r--;
				}
				while(b!=0){
					cout<<"Y"<<"B";
					b--;
				}
			}
		}
		else if(x==b){
			if(x>r+y){
				cout<<"IMPOSSIBLE";			
			}
			else {
				while(x!=(r+y)){
					if(r>y){
						cout<<"B"<<"R"<<"Y";
					}
					else{
						cout<<"B"<<"Y"<<"R";
					}
					r--;
					y--;
					x--;
				}
				while(r!=0){
					cout<<"B"<<"R";
					r--;
				}
				while(y!=0){
					cout<<"B"<<"Y";
					y--;
				}
			}
		}
		cout<<endl;
		
	}
	
}