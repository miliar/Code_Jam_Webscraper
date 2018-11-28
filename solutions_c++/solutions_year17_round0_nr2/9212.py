#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define debug(x,y) cout<<x<<y
#define NL printf("\n")
#define SP printf(" ")


int main(){
	int tcase;
	cin>>tcase;
	for(int t=1;t<=tcase;t++){
		long long n,numb=0;
		cin>>n;
		long long temp=n;
		vector<int> arr;
		while(temp!=0){
			arr.push_back(temp%10);
			temp/=10;
		}
		reverse(arr.begin(),arr.end());
		int a=0,pos,num[20];
		memset(num,0,sizeof(num));
		int i=0;
		for(;i<arr.size();i++){
			if(a<arr[i]){
				num[i]=arr[i];
				a=arr[i];
				pos=i;
			} else if(a==arr[i]){
				num[i]=arr[i];
				a=arr[i];
			} else{
				num[pos]--;
				i=pos+1;
				break;
			}
		}
		for(;i<arr.size();i++){
			num[i]=9;
		}
		numb=0;
		for(i=0,pos=arr.size()-1;i<arr.size();i++,pos--){
			long long tmp=(num[i]*pow(10,pos));
			numb=numb+tmp;
			//cout<<numb<<" "<<tmp<<endl;
		}
		cout<<"Case #"<<t<<": "<<numb;
		NL;
	}
	return 0;
}