#include <bits/stdc++.h>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define UP upper_bound
#define LB lower_bound
#define LL long long 
#define Pi 3.14159265358
#define si size()
#define en end()
#define be begin()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii set<int>::iterator
#define Tree int ind, int L, int R
#define Left 2*ind,L,(L+R)/2
#define Right 2*ind+1,(L+R)/2+1,R
using namespace std;
main(){
	   freopen("txt.in","r",stdin);
	   freopen("txt.out","w",stdout);
	   int T;
	   cin>>T;
	   for(int t=1;t<=T;t++){
	   	int n, m;
	   		cin>>n>>m;
	   		string s[n+1];
	   		for(int i=1;i<=n;i++){
	   			cin>>s[i];	
			}
			int str=0;
			for(int i=1;i<=n;i++){
				char c='?';
				for(int j=0;j<m;j++){
					if(s[i][j]!='?'){
						c=s[i][j];
						str=i;
					}
					s[i][j]=c;
				}	
				for(int j=m-1;j>=0;j--){
					if(s[i][j]!='?'){
						c=s[i][j];
						str=i;
					}
					s[i][j]=c;
				}
			}

			for(int i=str-1;i>=0;i--){
				for(int j=0;j<m;j++){
					if(s[i][j]=='?')s[i][j]=s[i+1][j];
				}
			}
			for(int i=str+1;i<=n;i++){
				for(int j=0;j<m;j++){
					if(s[i][j]=='?')s[i][j]=s[i-1][j];
				}
			}
	   		cout<<"Case #"<<t<<": "<<endl;
	   		for(int i=1;i<=n;i++)cout<<s[i]<<endl;
	   }
	   }	
