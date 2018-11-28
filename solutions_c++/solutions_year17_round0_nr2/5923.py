#include <stdio.h>
#include <iostream>
#include <cstdlib>
using namespace std;
string a;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
int T;
	cin>>T;
	for(int cs=1;cs<=T;cs++){
		cin>>a;
		if(a.size()==1){
			cout<<"Case #"<<cs<<": "<<a<<endl;
			continue;
		}


		for(int i=0;i<a.size()-1;i++){
			if(a[i]>a[i+1]){
				int now = i;
				while(now!=0 && a[now]==a[now-1]){
					now--;
				}
				a[now]--;

				for(int j=now+1;j<a.size();j++)
					a[j]='9';
			}
		}
		cout<<"Case #"<<cs<<": ";
		if(a[0]!='0')cout<<a[0];
		for(int i=1;i<a.size();i++){
			cout<<a[i];
		}
		cout<<endl;
	}


	return 0;
}
