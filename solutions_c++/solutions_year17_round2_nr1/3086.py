#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main(int argc, const char * argv[]) {
    freopen ("/Users/utkarsh/Xcode_C++/Random/Random/BLAH1111/BLAH1111/i.txt","r",stdin);
    freopen ("/Users/utkarsh/Xcode_C++/Random/Random/BLAH1111/BLAH1111/o.txt","w",stdout);
    int t;
    cin>>t;
    for(int a=1;a<=t;a++)
    {
        long long d,n;
        long double max=-1;
        long long k,s;
        long double x;
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            cin>>k>>s;
            x=((long double)(d-k))/(long double)(s);
            if(x>max)
                max=x;
        }
        
        
        
        cout<<"Case #"<<a<<": "<<fixed<<setprecision(10)<<(long double)(d)/(long double)(max)<<endl;
    }
    
}


