#include<iostream>
#include<cstring>
#include<cmath>

using namespace std;

int main(){
	
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{

		string s;
		cin>>s;
		int size= s.size();
		int count=0;
		int arr[size];
		if(size==1){
			cout<< "Case #" << j <<": "<<s<<"\n";
			continue;
		}
		for(int i=0;i<size;i++){
			arr[i]=(s[i]-'0');
		}
		for(int i=0;i<size-1;i++){
			if(arr[i]<arr[i+1]){
				count=0;
			}
			else if(arr[i]==arr[i+1]){
				count++;
			}
			else if(arr[i]>arr[i+1]){
				if(count==0){
					arr[i]=arr[i]-1;
				}
				else{
					arr[i-count]=arr[i-count]-1;
					for(int m=i-count+1;m<=i;m++){
						arr[m]=9;
					}
				}
				for(int t=i+1;t<size;t++){
					arr[t]=9;
				}
				break;
			}
		}
	int flag=0;
	cout<<"Case #" << j<<": ";
	for(int i=0;i<=size-1;i++){
		if(flag==0 && arr[i]==0){
			continue;
		}
		else{
			flag=1;
			cout<<arr[i];
		}
	}
	cout<<"\n";

	}
}