#include<iostream>
#include<string>
using namespace std;

int main()
{
int t,k;
cin>>t;
for(k=1;k<=t;k++)
{
long long int l,i,j,m;
string str;
cin>>str;
l=str.length();
for(i=1;i<l;i++)
{
    if(str[i-1]>str[i])
    {
        str[i-1]=str[i-1]-1;
        for(j=i;j<l;j++)
        {
            str[j]='9';
        }
        str[j]='\0';
    
        for(m=i-1;m>0;m--)
    {
    	if(str[m-1]>str[m])
    	{
    		str[m]='9';
    		str[m-1]-=1;
    	}
    }
        
        break;

    }
}
cout<<"Case #"<<k<<": "<<stol(str)<<"\n";
}
return 0;

}
