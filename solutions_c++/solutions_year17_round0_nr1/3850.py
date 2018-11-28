//Yahoo

#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;


int main(){
	int T;
	cin>>T;
	int arr[1000+100];
	for(int Test=1;Test<=T;Test++){
		char c;
		int len=0;
		for(;;){
			scanf("%c",&c);
			if(c==' ')
				break;
			if(c=='-')
				arr[len++]=0;
			else
				arr[len++]=1;
		}
		int k;
		cin>>k;
		int ans=0;
		for(int i=0;i<=len-k;i++){
			if(arr[i]==0){
				for(int j=i;j<i+k;j++)
					arr[j]=1-arr[j];
				ans++;
			}
		}
		bool impossible=false;
		for(int i=len-k+1;i<len;i++){
			if(arr[i]==0)
				impossible=true;
		}
		cout<<"Case #"<<Test<<": ";
		if(impossible)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
}
