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
int main(){
	fileinput("A-large.in");
	filewrite("output.txt");
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		string s;
		int k;
		cin>>s>>k;
		int ans=0;
		for(int i=0;i<s.size()-k+1;i++){
			if(s[i] == '-'){
				ans++;
				for(int p=i;p<i+k;p++){
					if(s[p] == '-'){
						s[p]='+';
					}
					else{
						s[p]='-';
					}
				}
			}
		}
		bool check=true;
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				check=false;
			}
		}
		if(check){
			cout<<"Case #"<<tt<<": "<<ans<<endl; 
		}
		else{
			cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl; 
		}
	}
	
	return 0;
}
