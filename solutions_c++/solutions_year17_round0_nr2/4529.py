#include <iostream>
#include<string>
using namespace std;

int main() {

	int t,len,x,y,i,j,max ,k;
	cin>>t;
	long long n ,m ,p;
	int st [1000];
	char str[1000] ;
	for(k=1;k<=t;k++)
		{
			cin>> n ;
			p=n;
			x=0;
			while(p!=0)
                {st[x++]=p%10;p=p/10;}
            for(i=0;i<x;i++)
                str[i]=st[x-i-1]+'0';
            str[x]='\0';
			//str =  to_string(n);
			len=x;
			x=0;
			for(i=0;i<len;i++)
					{
						if(x<str[i]-'0')
						{
							x=str[i]-'0';
						}
						else if (x>str[i]-'0')
						{
							break;
						}
					}
			if(i== len){
cout<<"case #"<<k<<": ";
				cout<<str<<endl ; continue ;
			}
			j=i-1;

			while(j>= 0 && str[j]==str[i-1])
				{
				  j--;
				}
			j++;
		//	cout<<n<<"  "<<i<<"   "<<j<<"   ";
			str[j]--;
			for(i=j+1;i<len;i++)
				str[i]='9';
			//m=stoi(str);
			i=0;
			while(str[i]=='0') i++;
			cout<<"case #"<<k<<": ";
			while(i<len) cout<<str[i++];
			cout<<endl;



		}



	return 0;
}
