#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
using namespace std;
#define ull unsigned long long
#define lli long long
#define mod 1000000007
map<tuple<string,int,int,int,int,int,int>,int > mp;

string start="";
int solved=0;
bool iscompat(string a,string b){
	if(a==b){
		return false;
	}
	if(a=="R" && b=="O") return false;
	if(a=="R" && b=="V") return false;
	if(a=="Y" && b=="O") return false;
	if(a=="Y" && b=="G") return false;
	if(a=="B" && b=="G") return false;
	if(a=="B" && b=="V") return false;
	return true;
}
int mm;
string rec(string pc,int n,int r,int o,int y,int g,int b,int v,string sol){
	if(n==0){
		if(iscompat(start,pc)){
			mp[make_tuple(pc,r,o,y,g,b,v)]=1;
			return sol;
		}
		else{
			mp[make_tuple(pc,r,o,y,g,b,v)]=-1;
			return "";
		}
	}
	if(mp[make_tuple(pc,r,o,y,g,b,v)]==-1){
		return "";
	}
	string got="";
	if(pc=="R"){
		if(y>0){
			got=rec("Y",n-1,r,o,y-1,g,b,v,sol+"Y");
			if(got!=""){
				return got;
			}
		}
		if(b>0){
			got=rec("B",n-1,r,o,y,g,b-1,v,sol+"B");
			if(got!=""){
				return got;
			}
		}
		else if(g>0){
			got=rec("G",n-1,r,o,y,g-1,b,v,sol+"G");
			if(got!=""){
				return got;
			}
		}
	}
	else if(pc=="Y"){
		if(b>0 && b>=r){
			got=rec("B",n-1,r,o,y,g,b-1,v,sol+"B");
			if(got!=""){
				return got;
			}
		}
		else if(r>0){
			got=rec("R",n-1,r-1,o,y,g,b,v,sol+"R");
			if(got!=""){
				return got;
			}
		}
		else if(v>0){
			got=rec("V",n-1,r,o,y,g,b,v-1,sol+"V");
			if(got!=""){
				return got;
			}
		}
	}
	else if(pc=="B"){
		if(r>0 && r>=y){
			got=rec("R",n-1,r-1,o,y,g,b,v,sol+"R");
			if(got!=""){
				return got;
			}
		}
		else if(y>0){
			got=rec("Y",n-1,r,o,y-1,g,b,v,sol+"Y");
			if(got!=""){
				return got;
			}
		}
		else if(o>0){
			got=rec("O",n-1,r,o-1,y,g,b,v,sol+"O");
			if(got!=""){
				return got;
			}
		}
	}
	else if(pc=="O" && b>0){
		got=rec("B",n-1,r,o,y,g,b-1,v,sol+"B");
		if(got!=""){
			return got;
		}
	}
	else if(pc=="G" && r>0){
		got=rec("R",n-1,r-1,o,y,g,b,v,sol+"R");		
		if(got!=""){
			return got;
		}
	}
	else if(pc=="V" && y>0){
		got=rec("Y",n-1,r,o,y-1,g,b,v,sol+"Y");
		if(got!=""){
			return got;
		}
	}

	
	mp[make_tuple(pc,r,o,y,g,b,v)]=-1;
	return "";	
}


void solve(int test_case_number){
solved=0;
mp.clear();
mm=0;
	 int n,r,o,y,g,b,v;
	 cin>>n>>r>>o>>y>>g>>b>>v;
	 if(r>0) start="R",r--;
	 else if(o>0) start="O",r--;
	 else if(y>0) start="Y",y--;
	 else if(g>0) start="G",g--;
	 else if(b>0) start="B",b--;
	 else if(v>0) start="V",v--;
	 n--;
	 if(n==0){
	 	cout<<start;
	 	return ;
	 }
	 string ans=rec(start,n,r,o,y,g,b,v,""); 

	if(ans==""){
		cout<<"IMPOSSIBLE";
	}
	else{
		cout<<start+ans;
	}
}

int main(){
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++){
		cout<<"Case #"<<tt<<": ";
		solve(tt);
		cout<<endl;
		cerr<<"solved "<<tt<<endl;
	}
	return 0;
}
