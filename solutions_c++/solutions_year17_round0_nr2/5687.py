#include <iostream>
using namespace std;

int main() {
    int t,q,f;
    long long int te,n,r,i;
    cin>>t;
    for(q=1;q<=t;q++)
    {
        cin>>n;
        while(1)
        {
            te=n;
            f=1;
            i=10;
            r=te%10;
            te/=10;
            while(te)
            {
               if((te%10)<=r)
                r=te%10;
               else
                {
                  f=0;
                  goto out;
                }
               te/=10;
               i=i*10;
            }
            out:
            if(f==0)
            {
                r=n%i;
                n=n-r-1;
            }
            else
             break;
        }
        cout<<"Case #"<<q<<": "<<n<<endl;
    }
    return 0;
}
