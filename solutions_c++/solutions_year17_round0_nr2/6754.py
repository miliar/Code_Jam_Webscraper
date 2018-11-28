#include<bits/stdc++.h>

using namespace std;

int main()
{
freopen("a.in", "r", stdin);
freopen("b.out", "w", stdout);
//cout<<"#0"<<endl;
int s[20];
long long int t,size,sp,T,n,k,ans,ansr,flag,i,j,num,temp,count;

cin>>t;

for(T=1;T<=t;T++)
{
	flag=0;
	//cout<<"#1"<<endl;
	for(i=0;i<20;i++)
	s[i]=0;
	
	cin>>num;
	count=0;
	
	while(num>0)
	{
		//cout<<"#2 "<<num<<" why"<<endl;
		temp=num%10;
		s[count]=temp;
		count++;
		num/=10;
	}
	//cout<<"#2"<<" "<<count<<endl;
	X:{};
	
	for(i=count-1;i>=1;i--)
	{
		if(s[i]>s[i-1])
		{
			s[i]--;
			
			for(j=i-1;j>=0;j--)
			s[j]=9;
			
			/*cout<<"Showtime "<<endl;
			for(sp=count-1;sp>=0;sp--)
			{
				cout<<s[sp];
			}*/
			//cout<<endl;
			flag=1;
			break;
		}
	}
	
	if(flag==1)
	{
		flag=0;
		goto X;
	}
	//cout<<"#3"<<endl;

	printf("Case #%lld: ",T);
	//cout<<"#4"<<endl;
	for(i=count-1;i>=0;i--)
	{
		if(s[i]==0 && i==(count-1))
		{}
		else
		cout<<s[i];
	}
	//cout<<"#5"<<endl;
	cout<<endl;
}


return 0;
}
