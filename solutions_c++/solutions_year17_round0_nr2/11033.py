#include <iostream>
#include<string>
using namespace std;
void modify(int &array, int j,int k )
{   
    
}
int main() {
	string str;
	
	int t;
	cin>>t;
	int temp=0;
	int array[50];
	array[0]=0;
	getline(cin,str);
	while(t--)
	
	{   temp++;
	    //cout<<t;
	    //getline(cin,str);
	    getline(cin,str);
	    //cout<<str;
	    for(int i=0;i<str.length();i++)
	        {
	            array[i]=(str[i])-'0';
	            //cout<<array[i];
	        }
	   if(str.length()>1)
	   {
	        for(int i=0;i<str.length();i++)
	        {
                if(array[i]>array[i+1])
                {   
                    array[i]=array[i]-1;
                    
                    
                    for (int j=i+1;j<str.length();j++)
                    {array[j]=9;}
                    i=i-2;
                }
	        }
	        	   }
	        cout<<"Case #"<<temp<<": ";
	        for(int i=0;i<str.length();i++)
	        {   
	            if (i==0&&array[i]==0)
	                    i=i+1;
	            cout<<array[i];    
	        }

	    //cout<<str<<"\n";
	    //cout<<str.length()<<"\n";
	    cout<<"\n";
    }
	
}

