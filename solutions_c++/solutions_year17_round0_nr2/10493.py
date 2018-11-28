#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i=0;i<n;i++)
    {
    	int no;
    	cin>>no;
    	for(int m=no;m>=0;m--)
    	{
    		int s;
    		s=(int)(log10(m))+1;
    		vector<int> d(s);
    		int h=m;
    		for(int j=s-1;j>=0;j--)
    		{
    			d[s-1-j]=h/pow(10,j);
    			
    			h=h-(((int)(h/pow(10,j)))*pow(10,j));
    			
    		}
    		int max=d[0];
    		int flag=0;
    		
    		for(int k=0;k<s;k++)
    		{
    			if(d[k]<max)
    			{
    				flag=1;
    				break;
    			}
    			else
    			max=d[k];
    		}
    	
    		if(flag==0)
    		{
    			cout<<"Case #"<<(i+1)<<": "<<m<<endl;
    			break;
    		}
    		
    	}
    }
    }