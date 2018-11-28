#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	    long int n,j,r1,r,m,c;
	    //cout<<1<<endl;
	    cin>>n;
	    //cout<<1<<endl;
	    if(n<10)
	    {
	        cout<<"case #"<<i<<": "<<n<<endl;
	    }
	    else
	    {
	        for(j=n;j>0;j--)
	        {
	            if(j<10)
	            {
	                cout<<"case #"<<i<<": "<<j<<endl;
	                break;
	            }
	            //cout<<1<<endl;
	            m=j;
	            r=m%10;
	            m=m/10;
	            while(m>0)
	            {
	                r1=m%10;
	                m=m/10;
	                if(r1<=r)
	                {
	                    c=1;
	                    r=r1;
	                }
	                else
	                {
	                    c=0;
	                    break;
	                }
	            }
	            if(c==1)
	            {
	                cout<<"case #"<<i<<": "<<j<<endl;
	                break;
	            }
	        }
	    }
	}
	return 0;
}
