#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("lolz.in","r",stdin);
	freopen("lolz.out","w",stdout);
	int t,i,j,k,it;
	cin>>t;
	char arr[1100];
	for(it=0;it<t;it++){

		cout<<"Case #"<<it+1<<": ";

		cin>>arr>>k;
		int len=strlen(arr);
		
		bool flip=false;
		int cnt=0;

		for(i=0;i<=len-k;i++){
			if(arr[i]=='-'){
				cnt++;
				for(j=i;j<i+k;j++){
					if(arr[j]=='-'){
						arr[j]='+';
					}else{
						arr[j]='-';
					}
				}
			}
		}
		for(i=0;i<len;i++){
			if(arr[i]=='-'){
				flip=true;
			}
		}
		if(flip){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<cnt<<endl;
		}
	}
	return 0;
}