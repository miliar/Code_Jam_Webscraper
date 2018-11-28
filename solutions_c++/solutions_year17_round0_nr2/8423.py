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

		cin>>arr;
		int len=strlen(arr);
		
		for(i=0;i<len-1;i++){
			int mini=arr[i]-48;
			int j=i+1;

			while(arr[j]==arr[i] && j<len){
				j++;
			}

			if(j<len)
			mini=min(mini,arr[j]-48);
			
			
			// cout<<mini<<endl;
			if(mini!=(int)(arr[i]-48)){
				arr[i++]--;
				
				for(;i<len;i++){
					arr[i]=57;
				}
			}	
		}
		bool flag=false;
		for(i=0;i<len;i++){
			if(flag || arr[i]!='0'){
				flag=true;
				cout<<arr[i];
			}
		}
		cout<<endl;
	}
	return 0;
}