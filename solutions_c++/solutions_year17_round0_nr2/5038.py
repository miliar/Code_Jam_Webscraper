#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll cc,i,j;
	int x,y;
	char z;
	string s;
	ll t;
	cin>>t;
	for(cc=1;cc<=t;cc++){
		s.clear();
		cin>>s;
		for(i=0;i<s.length()-1;i++){
			x=s[i]-'0';
			y=s[i+1]-'0';
			if(x>y){
				for(j=i+1;j<s.length();j++){
					s[j]='9';
				}
				z='0'+x-1;
				s[i]=z;
				for(j=i;j>0;j--){
					x=s[j]-'0';
					y=s[j-1]-'0';
					if(x<y){
						s[j]='9';
						z='0'+y-1;
						s[j-1]=z;
					}
				}
				break;
			}	
		}
		cout<<"Case #"<<cc<<": ";
		for(i=0;i<s.length();i++){
			if(s[i]=='0')continue;
			cout<<s[i];
		}
		cout<<endl;
	}

	return 0;
}
