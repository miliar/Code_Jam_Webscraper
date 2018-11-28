#include<iostream>
using namespace std;
int main (){
		int t;
		cin>>t;
		int count=0;
		long long counter;
		int arr[1000005];
		while(t--){
				count++;
				string cake;
				cin >>cake;
				for (int i=0;i<cake.length();i++){
						if (cake[i]=='-') arr[i]=0;
						else arr[i]=1;
				}
				int k;cin >>k;
				int len=cake.length();
				int ans=0;
				for (int i=0;i<len;i++){
						if (i>len-k){
								if (!arr[i]){
										cout<<"case #"<<count<<": IMPOSSIBLE"<<endl;
										goto fnc;
								}
						}
						else {
								if (!arr[i]) {
										ans++;
										for (int j=i;j<i+k;j++)
												if (arr[j]) arr[j]=0;
												else arr[j]=1;
								}
						}
				}
				cout<<"case #"<<count<<": "<<ans<<endl;
fnc: counter++;
		}
		return 0;
}


