#include <iostream>
#include <vector>

using namespace std;

int main() {
	long long int n,i,j,num,k,myint,z;
	vector<int> myvector;
	cin>>n;

	for(i=0;i<n;i++)
	{
	    k=0;
	    cin>>num;
	    while(num>0)
	    {
	        
	        myint=num%10;
	        myvector.push_back (myint);
	        num=num/10;
	        k++;
	    }
	    for(j=0;j<k-1;j++)
	    {
	        if(myvector.at(j)<myvector.at(j+1))
	        {
	            
	            for(z=j;z>=0;z--)
	            {
	               
	                myvector.at(z)=9;
	            }
	            myvector.at(j+1)=myvector.at(j+1)-1;
	        }
	    }
	    num=0;
	    for(j=k-1;j>=0;j--)
	    {
            num=num*10+myvector.at(j);	        
	    }
	    cout<<num<<"\n";
	     while (!myvector.empty())
          {
             myvector.pop_back();
          }
	}
	
	return 0;
}
