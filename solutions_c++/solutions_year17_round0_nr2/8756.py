#include <iostream>
#include <math.h>
using namespace std;
bool final(long long int n)
{
	long long int x;
    long long int l=log10(n)+1;
     for(long long int i=1;i<l;i++)
 {
      x=n%10;
     n=n/10;
     long long int y=n%10;
     if(x<y)
        {
            return false;
            }

}
return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    long long int t;
    cin>>t;
    long long int k=1;
    while(k<=t)
    {
        long long int n;
        cin >>n;
        if(final(n)==true)
        {
            cout<<"Case #"<<k<<": "<<n<<endl;
            ++k;
            continue;
        }
        //Case #3: 7
        long long int x=(n%10)+1;
       
        n=n-x;
        
       //long long int f=1;
       long long int p=1,f=10;
            for(long long int i=n;i>=9;i=i-p)
            {
            	//cout<<i<<endl;
                if(final(i)==true)
                    {
                        cout<<"Case #"<<k<<": "<<i<<endl;
                        break;
                    }
                     f=f*10;
                    p=(i%f)+1;
            }
      // }
       
       ++k;
       
    }
    return 0;
}
