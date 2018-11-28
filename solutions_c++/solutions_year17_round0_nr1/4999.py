#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ALarge.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
    	string str;
    	int k;
    	cin>>str>>k;
    	int n=str.length();
    	int c=0;
    	for(int i1=0;i1<=n-k;i1++){
    		if(str[i1]=='-'){
    			int j=i1;
    			c++;
    			 for(int i2=j;i2<j+k;i2++){
    			 	if(str[i2]=='+')
    			 	str[i2]='-';
    			 	else if(str[i2]=='-')
    			 	str[i2]='+';
    			 }
    			 
    		}
    	}
    	int flag=0;
    	for(int i1=0;i1<n;i1++){
    		if(str[i1]=='-')
    		flag=1;
    	}
    	if(flag==0)
    	cout<<"Case #"<<i<<": "<<c<<endl;
    	else
    	cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }

	return 0;
}

