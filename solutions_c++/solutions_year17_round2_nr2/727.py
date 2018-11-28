#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		cout<<"Case #"<<tc<<": ";
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		
		if(r==n || o==n || y==n || g==n || b==n || v==n){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}

		if(r+g==n){
			if(r==g){
				for(int i=0; i<n; i++){
					if(i%2==0)
						cout<<'R';
					else
						cout<<'G';
				}
				cout<<endl;
			}
			else{
				cout<<"IMPOSSIBLE"<<endl;
			}
			continue;
		}
		
		if(b+o==n){
			if(b==o){
				for(int i=0; i<n; i++){
					if(i%2==0)
						cout<<'B';
					else
						cout<<'O';
				}
				cout<<endl;
			}
			else{
				cout<<"IMPOSSIBLE"<<endl;
			}
			continue;
		}
		
		if(y+v==n){
			if(y==v){
				for(int i=0; i<n; i++){
					if(i%2==0)
						cout<<'Y';
					else
						cout<<'V';
				}
				cout<<endl;
			}
			else{
				cout<<"IMPOSSIBLE"<<endl;
			}
			continue;
		}
		
		if( (v!=0 && y<=v) || (o!=0 && b<=o) || (g!=0 && r<=g) ){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}

		r -= g;
		b -= o;
		y -= v;

		int m = r+b+y;
		char h[m];
		for(int i=0; i<m; i++)
			h[i] = 'E';

		if(r>b+y || b>r+y || y>r+b){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		
		//cout<<r<<" "<<y<<" "<<b<<endl;
		
		if(y>b && y>r){
			int p = 0;
			while(y>0){
				h[p] = 'Y';
				y--;
				p += 2;
				//cout<<p<<" ";
			}
			
			p = m-1;
			while(b>0){
				if(h[p]!='E'){
					p--;
				}
				else{
					h[p] = 'B';
					b--;
					p -= 2;
				}
				//cout<<p<<" ";
			}
			
			p = 0;
			while(r>0){
				if(h[p]!='E'){
					p++;
				}
				else{
					h[p] = 'R';
					r--;
					p += 2;
				}
				//cout<<p<<" ";
			}
		}
		else{
			int p = 0;
			while(r>0){
				h[p] = 'R';
				r--;
				p += 2;
				//cout<<p<<" ";
			}
			
			p = m-1;
			while(b>0){
				if(h[p]!='E'){
					p--;
				}
				else{
					h[p] = 'B';
					b--;
					p -= 2;
				}
				//cout<<p<<" ";
			}
			
			p = 0;
			while(y>0){
				if(h[p]!='E'){
					p++;
				}
				else{
					h[p] = 'Y';
					y--;
					p += 2;
				}
				//cout<<p<<" ";
			}
		}
		
		for(int i=0; i<m; i++){
			cout<<h[i];
			if(h[i]=='R' && g>0){
				for(int j=0; j<g; j++)
					cout<<"GR";
				g == 0;
			}
			if(h[i]=='B' && o>0){
				for(int j=0; j<o; j++)
					cout<<"OB";
				o == 0;
			}
			if(h[i]=='Y' && v>0){
				for(int j=0; j<v; j++)
					cout<<"VY";
				v == 0;
			}
		}
		cout<<endl;
	}
}