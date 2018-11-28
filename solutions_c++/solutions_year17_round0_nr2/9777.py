
#include <bits/stdc++.h>
#include <math.h>
//#include <boost/multiprecision/cpp_int.hpp>
//using boost::multiprecision::int128_t;
using namespace std;

int main() {
	// your code goes here
	int t; cin >> t;
    for(int x=1;x<=t;x++)
    {
        string n;
        cin>>n;
        int l = n.length();

        for(int i=l-1;i>0;i--)
        {
        	int a=(int)(n[i-1]-'0');
        	int b=(int)(n[i]-'0');
        	//cout<<a<<" "<<b<<endl;
        	if(a>b)
        	{
        		n[i-1]=n[i-1]-1;
        		n[i]='9';
        	}
        }

        int flag1=0;
        for(int i=0;i<l;i++)
        {
            if(n[i]!='0')
            {
                break;
            }
            if(n[i]=='0')
            {
                flag1=i+1;
            }
        }
        int flag2 = l;
        for(int i=0;i<l;i++)
        {
            if(n[i]=='9')
            {
                flag2=i;
                break;
            }
        }

        cout<<"Case #"<<x<<": ";
        for(int i=flag1;i<flag2;i++)
        {
        	cout<<n[i];
        }
        for(int i=flag2;i<l;i++)
        {
        	cout<<"9";
        }
        cout<<endl;
    }
	return 0;
}
