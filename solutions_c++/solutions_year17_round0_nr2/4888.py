#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int t,l;
	string s;
	scanf("%d",&t);
	cin.ignore();
	for(int m=1;m<=t;m++){
		cin>>s;
		l=s.size();
		for(int i=0;i<(l-1);i++){
				if(s[i]>s[i+1]){
					s[i]=s[i]-1;
					for(int j=(i+1);j<l;j++){
						s[j]='9';
					}
					for(int j=(i-1);j>=0;j--){
						if(s[j]>s[j+1]){
							s[j]=s[j]-1;
							s[j+1]='9';
						}
					}
					if(s[0]=='0'){
						s[0]='9';
						s[l-1]=' ';
					}
					break;
				}
				
			}
		cout<<"Case #"<<m<<": "<<s<<endl;
	}
	return 0;
}
