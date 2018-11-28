#include<iostream>
#include<string>


using namespace std;


//void p(string s){
//	for(int i=s.length()-1;i>=0;i--)
//		cout<<s[i];
//}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Boutlarge.in","w",stdout);
	long unsigned t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		
//		unsigned long long num;
		
		
		
		char left,right;
		string num;
		int flag=0;
		
		cin>>num;
//		cout<<num<<endl;
//		 int perf=num.length()-1;
		while(!flag){
			flag=1;
			for(int j=0;j<num.length()-1;j++){
				if(num[j]>num[j+1]){
					flag=0;
					num[j]=num[j]-1;
					num[j+1]='9';
//					cout<<num[j]<<" "<<num[j+1];
					for(int k=j+2;k<num.length();k++)
						num[k]='9';
				}
				
			}
		}
//		
//		for(int j=num.length()-1;j>0;j--){
//			right=num[j];
//			left=num[j-1];
//			if(left>right||right=='0'){
//				num[j]='9';
//				if(left!=0)
//					num[j-1]=left-1;
//			}
//			
//		}	
//	
	if(num[0]=='0')
		num.erase(num.begin());
	
//		while(num>0){
//			
//			units=num%10;
//			num/=10;
//			tens=num%10;
//			if(tens>units||units==0){
//				units=9;
//				tens=tens-1;
//			}
////			cout<<units;
//			s[j++]=units+'0';
//			num=(num/10)*10+tens;
//			cout<<units<<" "<<tens<<" "<<num<<endl;
//		}
//		
		if(i==t){	
			cout<<"Case #"<<i<<": "<<num;
			}
			
			
		else
		{	cout<<"Case #"<<i<<": "<<num<<endl;
			}
			
	}
}
