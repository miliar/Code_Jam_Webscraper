#include<iostream>
using namespace std;
int main(){
	freopen("B-small-attempt2.in","r",stdin);
	//freopen("A-large-practice.in","r",stdin);
	freopen("Google1.out","w",stdout);
	int T,N;
	int i,j,rem,rem1,temp,temp2,flag=0;
	cin>>T;
	for(i=0;i<T;i++){
		cin>>N;
		for(j=N;j>=0;j--){
			temp2=j;
			while(temp2!=0){
				rem=temp2%10;
				temp=temp2/10;
				while(temp!=0){
					if(temp==0)
						break;
					rem1=temp%10;
					if(rem<rem1){
						flag=0;
						break;
					}
					else if(rem>=rem1)
						flag=1;
					temp=temp/10;
				}
				temp2=temp2/10;	
				if(flag==0)
					break;
			}
			if(flag==1 || temp==0){
					cout<<"Case #"<<i+1<<": "<<j<<endl;
					break;				
			}
		}
	}
	return 0;
}
