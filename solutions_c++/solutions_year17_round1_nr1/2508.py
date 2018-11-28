#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
using namespace std;


int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	ll t,r,c,i,j,k=1;
	string s[30];
	ifstream infile;
	ofstream outfile;
	infile.open("A-large (1).in");
	outfile.open("output.txt");
	infile>>t;
	while(t--){
		ll a[30],b,p=0;
		for(i=0;i<30;i++) a[i]=-1;
		infile>>r>>c;
		for(i=0;i<r;i++) infile>>s[i];
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				if(s[i][j]=='?') p++;
			}
		}
		outfile<<"Case #"<<k<<": "<<endl;
		if(p==0){
			for(i=0;i<r;i++) outfile<<s[i]<<endl;
		}
		else if(p==r*c){
			for(i=0;i<r;i++){
				for(j=0;j<c;j++) outfile<<char('A'+i);
				outfile<<endl;
			}
		}
		else{
			for(i=0;i<r;i++){
			for(j=0;j<c;j++) if(s[i][j]!='?'){
				a[i]=j;break;
			}
		}
		for(i=0;i<r;i++){
			if(a[i]!=-1){
				for(j=0;j<c;j++){
					if(s[i][j]=='?') s[i][j]=s[i][a[i]];
					else a[i]=j;
			    }
			}
		}
		for(i=0;i<r;i++){
			if(s[i][0]!='?'){
				b=i;break;
			}
		}
	
		for(i=0;i<r;i++){
			if(a[i]==-1){
				s[i]=s[b];
			}
			else b=i;
		}
		for(i=0;i<r;i++) outfile<<s[i]<<endl;
		}
		k++;
	}
	return 0;
}
