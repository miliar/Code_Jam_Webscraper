#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++){
	char s[1001];
	int n,i,j,count=0,flag=0;
	string r;
	cin>>s>>n;
	r=s;
	for(i=0;i<=r.length()-n;i++){
		if(s[i]=='-'){
			count++;
			for(j=i;j<i+n;j++){
				s[j]=s[j]=='-'?'+':'-';
			}
		}
		//cout<<s<<endl;
	}
	for(i=0;i<r.length();i++)
		if(s[i]=='-'){
			cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
			flag=1;
			break;
		}
	if(flag==0)	
	cout<<"Case #"<<k<<": "<<count<<endl;
		
	}
	fclose(stdout);
	return 0;
}
