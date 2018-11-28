#include<bits/stdc++.h>
using namespace std;

int t, n;
string st;
bool dng;

int main(){
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	
	cin>>t;
	
	for(int tt=1; tt<=t; tt++){
		cin>>st;
		n = st.length();
		
		dng=false;
		for(int i=0; i<n; i++){
			if(dng){
				st[i] = '9';
			}
			else if(i!=n-1 && ((st[i]-'0') > (st[i+1]-'0'))){
				
				st[i]--;
				int j=i-1;
				while(j>=0 && st[j] > st[j+1]){
					st[j]--;
					j--;
				}
				j++;
				while((++j)<=i){
					st[j]='9';
				}
				dng = true;
			}
			
//			cout<<"i="<<i<<" st="<<st<<"\n";
		}
		
		if(st[0]=='0'){
			st="";
			while(--n){
				st+='9';
			}
		}
		
		cout<<"Case #"<<tt<<": "<<st<<"\n";
	}
}
