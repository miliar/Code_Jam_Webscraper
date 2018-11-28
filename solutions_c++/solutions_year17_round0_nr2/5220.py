#include<bits/stdc++.h>

using namespace std;

int position;
std::string to_string(int i)
{
    std::stringstream ss;
    ss << i;
    return ss.str();
}
template <class T>
int numDigits(T number)
{
    int digits = 0;
    if (number < 0) digits = 1;
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}
bool isNonDecrising(long long int number)
{
    int n=numDigits(number);
    string s=to_string(number);
    
    bool istrue=true;
    for(int i=0;i<n-1;i++)
    {
        if(s[i+1]<s[i])
        {
            istrue=false;
            position=i;
            break;
        }
    }
    return istrue;
}
long long int numberFrom(long long int number,int index)
{
    int length=numDigits(number);
    return (number % (long long int)(pow(10,(length-index-1)) ) );
}
int main()
{
    int t;
    cin>>t;
    position=0;
    for(int i=1;i<=t;i++)
    {
        long long int ans=0;
        cin>>ans;
        while(!isNonDecrising(ans))
        {
            long long int leftpart=numberFrom(ans,position);
            ans=ans-(leftpart)-1;
        }
        cout<<"Case #"<<i<<": "<<ans<<"\n";
        
    }
    return 0;
}