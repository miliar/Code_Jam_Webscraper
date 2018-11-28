#include <iostream>
using namespace std;

int isTidy(int n)
{
    int d1,d2;
    while(n)
    {
        d1 = n%10;
        n/=10;
        d2 = n%10;
        if(d1<d2)
            return 0;
    }
    return 1;
}
int main() {
	// your code goes here
	int t,count = 1;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int i;
	    for(i = n; i>0; i--)
	    {
	        if(isTidy(i))
	            break;
	    }
	    cout<<"Case #"<<count++<<": "<<i<<endl;
	}
	return 0;
}
