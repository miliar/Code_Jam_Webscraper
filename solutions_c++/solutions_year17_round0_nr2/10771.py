#include <iostream>
#include <math.h>
using namespace std;
bool final(int n)
{
     int l=log10(n)+1;
     for(int i=1;i<l;i++)
 {
     int x=n%10;
     n=n/10;
     int y=n%10;
     if(x<y)
        {
            return false;
            }

}
return true;
}
int main()
{
    freopen("B-small-attempt6.in.","r",stdin);
	freopen("output.txt","w",stdout);
    //cout << "Hello world!" << endl;
    int t;
    cin>>t;
    int k=1;
    while(k<=t)
    {
        int n;
        cin >>n;
        if(final(n)==true)
        {
            cout<<"Case #"<<k<<": "<<n<<endl;
            ++k;
            continue;
        }
        //Case #3: 7
        int x=(n%10)+1;
        n=n-x;
        if(final(n)==true)
            cout<<"Case #"<<k<<": "<<n<<endl;
        else
       {
            for(int i=n;i>=9;i=i-10)
            {
                if(final(i)==true)
                    {
                        cout<<"Case #"<<k<<": "<<i<<endl;
                        break;
                    }
            }
       }
       
       ++k;
       
    }
    return 0;
}
