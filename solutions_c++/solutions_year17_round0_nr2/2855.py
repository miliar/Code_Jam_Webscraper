#include <bits/stdc++.h>

using namespace std;
string str,ans;
int T;
int main(){
	cin>>T;
	int i,j,k,t;
	for (t=0;t<T;t++){
		cin>>str;
		j=str.size();
		for (i=1;i<str.size();i++){
			if (str[i]<str[i-1]){
				for (j=i;j>0;j--)
					if (str[j-1]<str[j])
						break;
			    str[j]--;
				break;
			}
		}
		if (str[0]!='0')ans=str[0];
		else ans="";
		for (i=1;i<str.size();i++)
			if(i<=j) ans=ans+str[i];
			else ans=ans+'9';	    
		cout<<"Case #"<<t+1<<": "<<ans<<"\n";
	}
	return 0;
}
