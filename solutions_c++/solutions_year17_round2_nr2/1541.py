#include<bits/stdc++.h>
using namespace std;

int t, n, r, y, b, o, g, v;
char rc, yc, bc, init;
string st;

int main(){
	ifstream cin("B-small-attempt2.in");
	ofstream cout("output.txt");
	
	cin>>t;
	for(int tt=1; tt<=t; tt++){
		cin>>n>>r>>o>>y>>g>>b>>v;
		
		rc='R', yc='Y', bc='B';
		
		if(r<y){
			swap(r, y);
			swap(rc, yc);
		}
		if(r<b){
			swap(r, b);
			swap(rc, bc);
		}
		if(y<b){
			swap(y, b);
			swap(yc, bc);
		}
//		cout<<"r="<<r<<" y="<<y<<" b="<<b<<"\n";
		if(r>(y+b)){
			cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
			continue;
		}
		
		init=rc;
		st="";
		st+=rc;
		r--;
		while(r>0 || y>0 || b>0){
			if(r<y || (r==y && yc==init)){
				swap(r, y);
				swap(rc, yc);
			}
			if(r<b || (r==b && bc==init)){
				swap(r, b);
				swap(rc, bc);
			}
			if(y<b){
				swap(y, b);
				swap(yc, bc);
			}
			if(rc!=st[st.length()-1]){
				st+=rc;
				r--;
			}
			else{
				st+=yc;
				y--;
			}
			
		}
		
		cout<<"Case #"<<tt<<": "<<st<<"\n";
	}
}
