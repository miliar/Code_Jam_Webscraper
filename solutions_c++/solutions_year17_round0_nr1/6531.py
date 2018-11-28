#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("/Users/rishabh-pc/Downloads/A-large.in","r",stdin);
    freopen("/Users/rishabh-pc/Desktop/cjq2yes1.txt","w",stdout);
    int t;
    cin>>t;
    int tcc=1;
    while(t--){
    	string s;
    	int k;
    	cin>>s;
    	cin>>k;
    	int n=s.length();
    	int i,j;
    	int count=0;
    	for(i=0;i<=(n-k);i++){
    		if(s[i]=='-'){
    			count++;
    			for(j=i;j<i+k;j++){
    				if(s[j]=='-')s[j]='+';
    				else s[j]='-';
				}
			}
		}
		for(i=0;i<n;i++){
			if(s[i]=='-')
			{
				break;
			}
		}
		cout<<"Case #"<<tcc++<<": ";
		if(i<n)cout<<"IMPOSSIBLE"<<endl;
		else
		cout<<count<<endl;
	}
    return 0;
}
