#include<iostream>

using namespace std;

int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;

	int k=t;

	while(t--){
		string num;

		cin>>num;

		for(int i=0;i<num.length()-1;i++){
			if(num[i]>num[i+1]){
				num[i]--;
				for(int j=i+1;j<num.length();j++)
					num[j]='9';
				int repeat = num[i]+1;
				if(i>0 && num[i-1]==num[i]+1)
					num[i]='9';
				for(int j=i-1;j>=0;j--){
					if(num[j]!=repeat)
						break;
					if(j==0 || num[j-1]!=num[j])
						{	num[j]--;
							break;
						}
					else num[j]='9';
				}
			}

		}

		int flag = 0;
			cout<<"Case #"<<k-t<<": ";	
		for(int i=0;i<num.length();i++){
			if(flag==0 && num[i]!='0'){
				flag=1;
			}
			if(flag==1){
				cout<<num[i];
			}

		}
		cout<<endl;
	}
}
