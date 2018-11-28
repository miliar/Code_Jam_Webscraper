#include<iostream>
using namespace std;
int main(){
		int t;
		cin >>t;
		int arr[1000005];
		int count=0;
		while(t--){
				count++;
				string s;
				cin >>s;
				cout<<"Case #"<<count<<": ";
				int len=s.length();
				for (int i=0;i<len;i++){
						arr[i]=s[i]-48;
				}
				for (int i=len-1;i>0;i--){
						if (arr[i]>=arr[i-1] && arr[len-1]!=0) continue;
						for (int j=i;j<len;j++)
								arr[j]=9;
						arr[i-1]-=1;
				}
				int flag=0;
				for (int i=0;i<len;i++){
						if (arr[i]!=0 || flag){
							flag=1;
							cout<<arr[i];
						}
				}
				cout<<endl;
		}
		return 0;
}
