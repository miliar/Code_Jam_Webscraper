#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int t,n;

	cin >> t;

    for(int i=1;i<=t;++i)
    {
       cin>>n;

       while(n > 0)
       {
       	string s=to_string(n);
       	if( is_sorted( s.begin() ,s.end()  ) ){ cout<<"Case #"<<i<<": "<<n<<"\n";break;}
       
        --n;
       }

    }
}