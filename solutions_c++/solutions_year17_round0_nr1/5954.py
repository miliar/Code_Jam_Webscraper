#include <stdio.h>
#include <iostream>
#include <cstdlib>
using namespace std;
string a;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int ans;
	int T;
	int k;
	cin>>T;
	for(int cs=1;cs<=T;cs++){
		cin>>a>>k;
		ans=0;

			for(int i=0;i<=a.size()-k;i++){
				if(a[i] =='-'){
							ans++;
					for(int j=i;j<i+k;j++){
						if(a[j]=='-')a[j]='+';
						else{
							a[j]='-';
						}
					}
				}
			}

		for(int i=0;i<a.size();i++){
			if(a[i]=='-'){
				ans =-1;
				break;
			}
		}
		if(ans==-1){
			cout<<"Case #"<<cs<<": IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<cs<<": "<<ans<<endl;
		}

	}


	return 0;
}
