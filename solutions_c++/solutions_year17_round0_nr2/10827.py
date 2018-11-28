#include <iostream>

using namespace std;




int main(){

	int t,k=1,m;
	char n[18];

	cin>>t;
	while(k<=t){
		cin>>n;
		int i=0,flag=0;
		while(n[i]!='\0'){
			if (flag==0)
			{
				if ((i+1)<18 && n[i+1]!='\0' && n[i+1] < n[i])
				{
					flag=1;
					n[i]--;
					if(i>0&&n[i]<n[i-1]){

						for(m=i;m>0;m--)
							n[m]='9';
						n[0]--;
					}
				}
			}else{
				n[i]='9';
			}
			i++;
		}
		cout<<"Case #"<<k<<": ";
		flag=0;
		for(i=0;n[i]!='\0';i++){
			if (flag==0)
			{
				if (n[i]>'0')
				{
					flag=1;
					cout<<n[i];
				}
			}else{
					cout<<n[i];
			}
		}
		//if (k!=t)
		//{
			cout<<endl;
		//}
		
		k++;

	}
	


	return 0;
}