#include<iostream>
using namespace std;
int check(int n)
{
	int temp = n%10;
	n/=10;
	n=n%10;
	if(n<=temp)
		return 1;
	else
		return 0;
}
int main()
{
	int n,t,ans,temp,num,k=1;
	cin>>t;
	while(t--)
	{ 
//		cout<<t;		
		cin>>n;
		if(n/10==0)
			cout<<"Case #"<<k++<<": "<<n<<endl;
		else{		
		ans=n/100;
		ans=ans*100 - 1;
		for(int i = ans+1;i<=n;i++)
		{	num = i;
			while(num){
//				cout<<num;
				temp = check(num);				
				if(temp==0)
					break;
				else
					num=num/10;			
			}
			if(num==0)
				ans = i;		
		}
			cout<<"Case #"<<k++<<": "<<ans<<endl;
		}
	}

 return 0;
}
