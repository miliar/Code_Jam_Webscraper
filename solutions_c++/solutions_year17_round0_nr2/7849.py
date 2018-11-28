#include <iostream>
#define MAX 1100

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int test=1; test<=t; test++)
	{
		string str;
		cin >> str;
		
		int flag = 0;
		int i;
		for( i = 0; i < str.length() - 1; i++)
		{
           if(str[i+1] - str[i] < 0)
           {
            	flag = 1;
            	break;
           }
        }
        if(flag)
        {
            for(int j=i+1; j<str.length(); j++)
            {
            	str[j]='9';
            }
            
            str[i] = (char) (str[i]-1);
           
            while( i>0 && str[i] < str[i-1])
            {
                str[i] = '9';
                str[i-1]--;
                i--;
            }
        }
        
        i=0;
    
        while(str[i]=='0')
             i++;
             
        cout<<"Case #"<< test <<':'<<' ';
        
       
        for(int k=i ; k < str.length(); k++)
        {    
        	cout << str[k];
        }
        cout<<endl;
	}
    return 0;
}