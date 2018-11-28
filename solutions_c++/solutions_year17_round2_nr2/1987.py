#include<bits/stdc++.h>
# define ll long long
# define ld long double 
using namespace std;
int main(){
	ios_base::sync_with_stdio();
	//cin.tie(0);
	//cout.tie(0);
	ll t,i;
	cin>>t;
	char ch[7];
		ch[0]='R';
		ch[1]='O';
		ch[2]='Y';
		ch[3]='G';
		ch[4]='B';
		ch[5]='V';
	
	for(i=1;i<=t;i++){
		ll n;
		cin>>n;
		int a[7];
		ll max=0;
		int in,j;
		for(j=0;j<6;j++){
			cin>>a[j];
			if(a[j]>max){
				max=a[j];
				in=j;
			}
		}
		string s;
		s.clear();
		//int prev=j;
		for(int j=0;j<n;j++){
			int max=0;
			for(int k=0;k<6;k++){
				if(a[k]>max&a[k]!=0){
					if(j>0){
						if(ch[k]!=s[j-1]){
						max=a[k];
						in=k;
						}
					}
					else{
						max=a[k];
						in=k;
					}
				}
				if(a[k]==max&&a[k]!=0&&ch[k]==s[0]){
					if(j>0){
						if(ch[k]!=s[j-1]){
						max=a[k];
						in=k;
						}
					}
					else{
						max=a[k];
						in=k;
					}

				}
			}
			s.push_back(ch[in]);
			a[in]--;
			int z=0;
			int nz=-1;
			for(int k=0;k<6;k++){
				if(a[k]==0)
					z++;
				else
					nz=k;
			}
			if(z==6)
				break;
			//cout<<s<<endl;
			if(z==5&&(ch[nz]==s[j]||ch[nz]==s[(j+2)%n])){
				s.clear();
				s="IMPOSSIBLE";
				break;
			}
		}
		cout<<"Case #"<<i<<": "<<s<<endl;
	}
return 0;
}