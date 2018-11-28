/*input

*/
#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	long long int tc=1,T;
	for(cin>>T;tc<=T;++tc){
		cout<<"Case #"<<tc<<": ";
		long long int n,r,o,y,g,b,v,k;
		cin>>n>>r>>o>>y>>g>>b>>v;
		long long int R=r+o+v,Y=y+o+g,B=b+g+v;
		string s="";
		for(k=0;k<n;++k){
			if(s==""){
				if(r) s+="R",r--;
				else if(b) s+='B',b--;
				else if(y) s+='Y',y--;
				else break;
				continue;
			}
			else if(s[s.size()-1]=='R'){
				if(g) s+='G',g--;
				else if(y&&y>=b) s+='Y',y--;
				else if(b&&b>y) s+='B',b--;
				else break;
			}
			else if(s[s.size()-1]=='Y'){
				if(v) s+='V',v--;
				else if(r&&r>=b) s+='R',r--;
				else if(b&&b>r) s+='B',b--;
				else break;
			}
			else if(s[s.size()-1]=='B'){
				if(o) s+='O',o--;
				else if(y&&y>=r) s+='Y',y--;
				else if(r&&r>y) s+='R',r--;
				else break;
			}
			else if(s[s.size()-1]=='O'){
				if(b) s+='B',b--;
				else break;
			}
			else if(s[s.size()-1]=='G'){
				if(r) s+='R',r--;
				else break;
			}
			else if(s[s.size()-1]=='V'){
				if(y) s+='Y',y--;
				else break;
			}
			if(k==n-1){
				if(s[0]=='R'||s[0]=='V'||s[0]=='O'){
					if(s[s.size()-1]=='R'||s[s.size()-1]=='O'||s[s.size()-1]=='V') break;
				}
				if(s[0]=='Y'||s[0]=='O'||s[0]=='G'){
					if(s[s.size()-1]=='Y'||s[s.size()-1]=='O'||s[s.size()-1]=='G') break;
				}
				if(s[0]=='B'||s[0]=='G'||s[0]=='V'){
					if(s[s.size()-1]=='B'||s[s.size()-1]=='G'||s[s.size()-1]=='V') break;
				}
			}
		}
		if(k<n) cout<<"IMPOSSIBLE\n";
		else cout<<s<<'\n';
	}
}