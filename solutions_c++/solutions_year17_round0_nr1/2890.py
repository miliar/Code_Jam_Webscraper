#include <bits/stdc++.h>

using namespace std;
string str;
int T,k;
int main(){
	int t,ans,i,j,c;
    cin>>T;
    for (t=0;t<T;t++){
		bool flag=1;
	    cin>>str>>k;
		c=ans=0;		
		for (i=0;i<str.size()-k+1;i++)
		    if (str[i]=='-'){
				ans++;
				for (int j=i;j<i+k;j++)
				    if (str[j]=='-') str[j]='+';
					else str[j]='-';
			}
		//cout<<str<<endl;
		for (i=0;i<str.size();i++)
			if (str[i]=='-')
				flag=0;
	    cout<<"Case #"<<t+1<<": ";
	    if (flag) cout<<ans<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
