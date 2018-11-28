#include<bits/stdc++.h>
using namespace std;

string check(string str,int index,string org)
{

    for(int i=index;i>=0;i--)
    {
		
        if(str[i]>str[i+1])
        {
            if(index==0)
            {

            if(str[i]=='1'&& str[i+1]=='0')
            {

                str[i]='0';str[i+1]='9';

				
            }
            else
            {
                str[i]-=1;
                str[i+1]='9';
				
            }
            }
            else
            {
                string temp=str;
                temp[i+1]=temp[i];
                if(temp<org)
				  str=temp;

                else
                {
                    str[i]-=1;
                    str[i+1]='9';
					
                }



            }
        }
    }
      return str;
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("output.out","w",stdout);
	int test;string str;
	cin>>test;
	//string s1="19 ,s2="1000";
	int m=1;
	while(test--)
	{
		cin>>str;
		string org=str;
		

            for(int i=1;i<str.size();i++)
            {
				//cout<<t<<endl;
                str=check(str,i-1,org);
            }
            cout <<"Case #"<<m<<": ";
           for(int i=0;i<str.size();i++)
            {

                if(str[i]!='0')
                    cout<<str[i];



            }
            cout<<endl;
			m++;
           //cout<<str<<endl;



	}
	return 0;
}
