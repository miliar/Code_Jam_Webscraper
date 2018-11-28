// AUTHOR VINAYAK SINGLA
#include<bits/stdc++.h>
using namespace std;
#define ff first 
#define ss second 
#define lli long long int
#define f(i,o,n) for(int i=o;i<n;i++)
int n,r,o,y,b,g,v,maxx;
string ans;
void solve(char c,char maj){
	if(r==0 && y==0 && b==0)return ;
	if(c=='r'){
		if(b==y && maj=='b'){
			ans=ans+"B";
			b--;
			solve('b',maj);
		}
		else if(b>y){
			ans=ans+"B";
			b--;
			solve('b',maj);
		}
		else{
			ans=ans+"Y";
			y--;
			solve('y',maj);
		}
	}
	else if(c=='b'){
		if(r==y && maj=='r'){
			ans=ans+"R";
			r--;
			solve('r',maj);
		}
		else if(r>y){
			ans=ans+"R";
			r--;
			solve('r',maj);
		}
		else{
			ans=ans+"Y";
			y--;
			solve('y',maj);
		}
	}
	else{
		if(r==b && maj=='b'){
			ans=ans+"B";
			b--;
			solve('b',maj);
		}
		else if(b>r){
			ans=ans+"B";
			b--;
			solve('b',maj);
		}
		else{
			ans=ans+"R";
			r--;
			solve('r',maj);
		}
	}
}

int main()
{
	int t;
	cin>>t;
    for(int k=0;k<t;k++){
        cin>>n>>r>>o>>y>>g>>b>>v;
        maxx=max(r,max(y,b));
        if(maxx>r+y+b-maxx){
        	cout<<"Case #"<<k+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			ans="";
			if(maxx==r){
				ans=ans+"R";
				r--;
				solve('r','r');
			}
			else if (maxx==b){
				ans=ans+"B";
				b--;
				solve('b','b');
			}
			else{
				ans=ans+"Y";
				y--;
				solve('y','y');
			}
        	cout<<"Case #"<<k+1<<": "<<ans<<endl;
		}
    }
    return 0;
}
