#include<iostream>
#include<math.h>
using namespace std;
int main(){
	freopen("B-small-attempt1.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
	int t,n[1000],len=1,temp,temp1,temp2=0,last;
	cout<"h";
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n[i];
		
		for(int j=0;j<=n[i];j++){
			temp=j;
			temp2=9;
			len=1;
			while(temp/=10)
				len++;
			temp=j;	
			for(int k=1;k<=len;k++){
				if(temp==0){
					last=0;break;
				}
				temp1=(temp%10);
				temp/=10;
				
				//cout<<temp1<<" "<<temp2<<endl;
				//cout<<len<<endl;
				if(temp2>=temp1&&k==len)
					last=j;
				if(temp2<temp1)
					break;
				temp2=temp1;
			}
		}
		cout<<"\nCase #"<<i+1<<": "<<last;
		last=1;
		
	}
	return 0;
}

