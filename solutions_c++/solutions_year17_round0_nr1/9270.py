#include<bits/stdc++.h>
using namespace std;
int main()
{
    //ofstream govind;
    //govind.open("code1.txt");
	long long int T,p=1;
	cin>>T;
	while(T>0)
	{
		
		string s;
		cin>>s;
		long long int k;
		cin>>k;
		int t=0,flag=0;
		for(int i=0;i<=s.length()-k;i++)
		{
			if(s[i]=='-')
			{
			 for(int j=i;j<i+k;j++)
			 {
				if(s[j]=='+')
				s[j]='-';
				else s[j]='+';
			 }
			 t++;
		    }
		}
		for(int i=s.length()-1;i>s.length()-k;i--)
		{
			if(s[i]=='-')
			{
				cout<<"case #"<<p++<<": IMPOSSIBLE"<<endl;
				//govind<<"case #"<<p++<<": IMPOSSIBLE"<<endl;
				flag=1;
				break;
			}
			
		}
		if(flag==0)
		cout<<"case #"<<p++<<": "<<t<<endl;
		//govind<<"case #"<<p++<<": "<<t<<endl;
		T--;
	}
        //govind.close();
}
