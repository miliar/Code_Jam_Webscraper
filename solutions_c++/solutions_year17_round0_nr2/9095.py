#include <iostream>
using namespace std;
int greatNum(int digit)
{
     int low=0;
    for(int i=1,j=1;i<=digit;i++)
    {
        low=low*10+i;
    }
    return low;
}
int digitCount(int n)
{
    int count=0;
    while(n)
    {
        count++;
        n/=10;
    }
    return count;
    
}
int leastNumber(int n)
{
    int digit=digitCount(n);
    int a=n;
    int low=0;
    for(int i=1;i<=digit;i++)
    {
        low=low*10+i;
    }
    //cout<<low;
    if(a<low)
    return greatNum(digit-1);
    else
    return low;
}
bool tidy(int n)
{
    int pre=n%10;
    int now;
    n/=10;
    while(n)
    {
        now = n%10;
        if(pre<now)return false;
        n/=10;
        pre=now;
    }
    return true;
}
int main() {
	// your code goes here
	int t;
	int s=1;
	cin>>t;
	while(s<=t)
	{
	    int n;
	    cin>>n;
	    int low=leastNumber(n);
	    //cout<<low<<endl;
	    cout<<"Case #"<<s<<": "; 
	    for(int i=n;i>=low;i--)
	    {
	        if(tidy(i))
	        {
	            cout<<i<<endl;
	            break;
	        }
	    }
	    s++;
	}
	return 0;
}
