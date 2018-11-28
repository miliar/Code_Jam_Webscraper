#define MOD 1000000007
#define P printf(" yes ")
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,j;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>t;
	for(j=1;j<=t;j++){
		string s;
		int k,count=0,cnt=0,i;
		cin>>s;
		cin>>k;
		for(i=0;i<s.length();i++){
			if(s[i]=='-')
			cnt++;
		}
		for(i=0;i<s.length();i++){
			if((s[i]=='-')&&(i+k<=s.length())){
				count++;
				s[i]='+';
				cnt--;
				for(int ii=1;ii<k;ii++){
					if(s[ii+i]=='+'){
						s[ii+i]='-';
						cnt++;
					}
					else{
						s[ii+i]='+';
						cnt--;
					}
				}
			}
		}
		//cout<<"count"<<count<<endl;
		if(cnt==0)
		cout<<"Case #"<<j<<": "<<count<<endl;
		else
		cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
	}
}

