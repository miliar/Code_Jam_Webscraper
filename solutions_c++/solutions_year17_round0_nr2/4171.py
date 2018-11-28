#include<bits/stdc++.h>
using namespace std;
string s;
int n, m, k, i, j, t;
string go_solve(string s){
	 string c=s;
	 bool bol=false;
	 for(int j=0;j<s.size()-1;j++){
		if(c[j]>c[j+1]){
		    c[j]--;
			j++;
			while(j<c.size())c[j]='9',j++;
			bol=true;
			break;
		}
	 }
//	 cout<<c<<endl;
//	 system("pause");
	 if(!bol)return c;
	 else return go_solve(c);
	 
}
main(){
	   freopen("alooo.in","r",stdin);
	   freopen("alooo.out","w",stdout);
	   cin>>t;
	   for(int i=1;i<=t;i++){
			cin>>s;
			s=go_solve(s);
 			cout<<"Case #"<<i<<": ";
 			for(int j=0;j<s.size();j++){
 				if(s[j]!='0'){
 					for(int k=j;k<s.size();k++)cout<<s[k];
 					break;
				 }
			 }
			 cout<<endl;
	   }
	   }
