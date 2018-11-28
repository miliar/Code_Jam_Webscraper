#include<bits/stdc++.h>
using namespace std;
string s;
int n, m, k, i, j, t, res;
priority_queue < pair < int , int > > q;
main(){
	   freopen("alooo.in","r",stdin);
	   freopen("alooo.out","w",stdout);
	   cin>>t;
	   for(int i=1;i<=t;i++){
			cin>>s>>k;
			bool bol=true;
			res=0;
			cout<<"Case #"<<i<<": ";
			for(int i=0;i+k<=s.size();i++){
				if(s[i]=='-'){
					for(int j=0;j<k;j++){
						s[i+j]=((s[i+j]=='+')?'-':'+');
					}
					res++;
				}
			}
			for(int i=0;i<s.size();i++){
				if(s[i]=='-'){
					bol=false;
					break;
				}
			}
			if(!bol){
				cout<<"Impossible\n";
			}
			else cout<<res<<endl;
			
	   }	   
	   }
	   
