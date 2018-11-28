#include <bits/stdc++.h>
using namespace std;
long  T,N;
int main(){
	cin>>T;
	for(int z=1;z<=T;z++){
		cin>>N;
		int n;
		printf("Case #%d: ",z);
		//cout<<"N="<<N<<" ans=";
		vector<int> number;
		while(N>0){
			number.push_back(N%10);
			N=N/10;
		}
		reverse(number.begin(),number.end());
		n=number.size();
		number.push_back(9);
		int i;
		for(i=0;i<n;i++)
			if(number[i]>number[i+1])
				break;
		while(i>=1 && number[i]==number[i-1] && i<n)
			i--;
		for(int j=i;j<number.size();j++){
			if(j==i)
				number[i]--;
			else
				number[j]=9;
		}
		long ans=0;
		for(int i=0;i<n;i++)
			ans=ans*10+number[i];
		cout<<ans<<endl;
		}
	return 0;	
	
}
