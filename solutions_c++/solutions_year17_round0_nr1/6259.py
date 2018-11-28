#include<bits/stdc++.h>
using namespace std;

int t, n, k, cnt;
bool pos;
string st;

int main(){
//	std::ios_base::sync_with_stdio(false);
//	cin.tie(0);
	
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	
	cin>>t;
	
	for(int tt=1; tt<=t; tt++){
		cin>>st>>k;
		n = st.length();
		
		cnt=0; pos=true;
		for(int i = 0; 1; i++){
			
			while(i<=(n-k) && (st[i]=='+')){
				i++;
			}
			
			if(i>(n-k)){
				break;
			}
			cnt++;
			for(int j=i; j<(i+k); j++){
				if(st[j]=='+') st[j] = '-';
				else st[j] = '+';
			}
			
//			cout<<"i="<<i<<" st="<<st<<"\n";
		}
		
		for(int i=n-k+1; i<n; i++){
			if(st[i]=='-'){
				pos = false;
				break;
			}
		}
		
		if(pos){
			cout<<"Case #"<<tt<<": "<<cnt<<"\n";
		}
		else{
			cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
		}
	}
}



