#include<iostream>
#include <stdio.h>
using namespace std;
int main(){
	freopen ("output.txt","w",stdout);
	freopen ("B-small-attempt3.in","r",stdin);
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		
		string s="";
		if(y==1 && r==0 && b==0 ) {
			cout<<"Y"<<endl;
			continue;
		}
		if(y==0 && r==0 && b==1 ) {
			cout<<"B"<<endl;
			continue;
		}
		if(y==0 && r==1 && b==0 ) {
			cout<<"R"<<endl;
			continue;
		}
		
		if(y>r+b){
			cout<<"IMPOSSIBLE"<<endl;
				continue;
		}
		if(r>y+b){
			cout<<"IMPOSSIBLE"<<endl;
				continue;
		}
		if(b>r+y){
			cout<<"IMPOSSIBLE"<<endl;
				continue;
		}

		char prev='Y';
		if(r>y && b>y) prev='Y';
		if(r>b && y>b) prev='B';
		if(y>r && b>r) prev='R';

		for(int j=0;j<n;j++){
			if(prev=='Y'){
				if(r>b){
					s+="R";
					prev='R';
					r--;
				}else{
					s+="B";
					prev='B';
					b--;
				}
			}else{
				if(prev=='B'){
				if(y>r){
					s+="Y";
					prev='Y';
					y--;
					
				}else{
					s+="R";
					prev='R';
					r--;
				}
				}else{
					if(prev=='R'){
					if(b>y){
						s+="B";
						prev='B';
						b--;
						
					}else{
						s+="Y";
						prev='Y';
						y--;
					}
					}
				}
				
			}
			
		}
		if(s[0]==s[s.length()-1]){
			char t=s[s.length()-1];
			s[s.length()-1]=s[s.length()-2];
			s[s.length()-2]=t;
		}
		cout<<s<<endl;
	}
	
	return 0;
}
