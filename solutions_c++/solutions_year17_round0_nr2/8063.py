#include <bits/stdc++.h>
using namespace std;
bool istidy(int arr[] , int n){
	int i;
	if(n==1){
		return true;
	}
	for( i=0;i<n-1;i++){
		if(arr[i]>arr[i+1]){
			return false;
		}
	}
	return true;
}

void reduceone(int arr[], int n, int pos){
	arr[pos]--;
	if(arr[pos]<0){
		arr[pos]+=10;
		reduceone(arr,n,pos-1);
	}
}

int main(){
	int i,t,j,n,arr[100],index,zerosofar;
	string l;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>l;
		n=l.size();
		if(n==1){
			cout<<"Case #"<<i+1<<": "<<l<<endl;
			continue;
		}
		for(j=0;j<n;j++){
			arr[j]=int(l[j]-48);
		}
		index=n-1;
		while(!istidy(arr,n)&&index>0){
			arr[index]=9;
			reduceone(arr,n,index-1);
			index--;
		}
		cout<<"Case #"<<i+1<<": ";
		zerosofar=1;
		for(j=0;j<n;j++){
			if(zerosofar==0){
				cout<<arr[j];
			}else if(zerosofar=1 && arr[j]!=0){
				zerosofar=0;
				cout<<arr[j];
			}
		}
		cout<<endl;
	}
	return 0;
}

