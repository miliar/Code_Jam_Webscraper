#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(0);cin.tie(0);
#define ff first
#define ss second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define PI 3.14159265
#define all(x) (x).begin(), (x).end()
#define fileinput(name) freopen((name),"r",stdin);
#define filewrite(name) freopen((name),"w",stdout);

bool cmp(const pair<int,int> &p1,const pair<int,int> &p2){
	return  p1.ss < p2.ss;
}
int r,o,y,g,b,v;
char tell(){
	char ma;
	if(r==0 && y==0 && b==0){
		return 'N';
	}
	if(r>=y && r>=b){
		ma='R';
		r--;
	}
	else if(y>=r && y>=b){
		ma='Y';
		y--;
	}
	else{
		ma='B';
		b--;
	}
	return ma;
}
int main(){
	fileinput("B-small-attempt2.in");
	filewrite("output.txt");
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		int n;
		cin>>n;
		cin>>r>>o>>y>>g>>b>>v;
		
		string ans="";
		bool flag=true;
		if(r>n/2 || y>n/2 || b>n/2){
			ans="IMPOSSIBLE";
			flag=false;
		}
		char temp=tell();
		while(flag&&n>1){
			n--;
			ans=ans+temp;
			if(temp == 'R'){
				if(y>=b){
					temp='Y';
					y--;
				}
				else{
					temp='B';
					b--;
				}
			}
			else if(temp == 'B'){
				if(r>=y){
					temp='R';
					r--;
				}
				else{
					temp='Y';
					y--;
				}
			}
			else{
				if(r>=b){
					temp='R';
					r--;
				}
				else{
					temp='B';
					b--;
				}
			}
		}
		if(flag){
			ans+=temp;
			if(ans[0] == ans[ans.size()-1]){
				char t=ans[ans.size()-1];
				ans[ans.size()-1]=ans[ans.size()-2];
				ans[ans.size()-2]=t;
			}
		}


		cout<<"Case #"<<tt<<": "<<ans<<endl; 
	}
	
	return 0;
}
