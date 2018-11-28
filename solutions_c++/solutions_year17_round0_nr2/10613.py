#include<iostream>
using namespace std;
int main(void)
{
int T=1,N=1,bit=1;
cin>>T;
for(int i=1;i<=T;i++)
{
bit=1;
cin>>N;
    if(N<=1000&&N>100){if(N==1000){N=999;}
	for(;bit==1;N--){if((N/100)<=(N/10)%10&&(N/10)%10<=(N%10)){bit=0;cout<<"Case #"<<i<<": "<<N<<endl;}}
	}
    if(N<=100&&N>10){if(N==100){N=99;}
	for(;bit==1;N--){if((N/10)<=(N%10)){bit=0;cout<<"Case #"<<i<<": "<<N<<endl;}}
	}
    if(N<=10){if(N==10){N=9;}
	cout<<"Case #"<<i<<": "<<N<<endl;
	}
}
return 0;
}
