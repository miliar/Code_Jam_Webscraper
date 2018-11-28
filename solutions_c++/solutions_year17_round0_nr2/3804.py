//Yahoo

#include<cstdio>
#include<iostream>
using namespace std;

int arr[100],len;
bool normalize(){
		for(int i=0;i<len-1;i++){
			if(arr[i]>arr[i+1]){
				arr[i]--;
				for(int j=i+1;j<len;j++)
					arr[j]=9;
				return true;
			}
		}
		return false;

}

int main(){
	int T;
	cin>>T;
	for(int Test=0;Test<=T;Test++){
		len=0;
		char c;
		while(true){
			scanf("%c",&c);
			if(c<'0' || c>'9')
				break;
			arr[len++]=c-'0';
		}
		while(normalize());
		if(len==0)
			continue;
		cout<<"Case #"<<Test<<": ";
		for(int i=0;i<len;i++){
			if(arr[i])
				cout<<arr[i];
		}
		cout<<endl;
	}


}
