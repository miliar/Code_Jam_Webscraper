#include<iostream>
#include<string>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nn;
	cin>>nn;
	int ii=0;
	while(ii<nn){
		string s;
		cin>>s;
		int num[20];
		for(int i=0;i<20;i++)num[i]=0;
		int len=0;
		for(int i=s.size()-1;i>=0;i--){
			num[len++]=s[i]-'0';
		}
		for(int i=0;i<len-1;i++){
			if(num[i]<num[i+1]){
				num[i+1]--;
				if(num[i+1]<0)
					for(int j=i+2;j<len;j++){
						num[j-1]+=10;
						num[j]--;
						if(num[j]>=0)break;
					}
				for(int j=0;j<=i;j++){
					num[j]=9;
				}
			}
		}
		cout<<"Case #"<<ii+1<<": ";
		bool start=0;
		for(int i=len-1;i>=0;i--){
			if(start==0&&num[i]==0)continue;
			else{
				start=1;
				cout<<num[i];
			}
		}
		cout<<endl;
		ii++;
	}

}
