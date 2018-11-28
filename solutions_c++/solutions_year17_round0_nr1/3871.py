// devsks 
//codeJam
//	08.04.2017
#include "bits/stdc++.h"

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		string st;
		int kk;
		cin>>st>>kk;
		int len = st.length(),flag=1,c=0,ans=0;
		for(int i=0;i<len;i++){
			if(st[i]=='-'){
				ans++;
				if(i+kk > len){
					flag=0;
					break;
				}
				for(int j = i; j < (i+kk);j++){
					st[j] = st[j] == '-' ? '+' : '-';
				}
			}
		}
		for(int i=0;i<len;i++)
			if(st[i]=='-'){
				flag=0;
				break;
			}
		cout<<"Case #"<<tt<<": ";
		if(!flag)
			puts("IMPOSSIBLE");
		else
			cout<<ans<<endl;
	}


	return 0;
}
