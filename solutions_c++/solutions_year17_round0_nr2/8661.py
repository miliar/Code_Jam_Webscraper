#include<bits/stdc++.h>
using namespace std;

int checkn(long long int n)
{
int flag=0,t=n%10;
n/=10;
while(n>0)
{
if(n%10>t)
{
flag=1;
break;
}
t=n%10;
n/=10;
}
if(flag==1)
return 1;
return 0;
}

int main()
{
    int t,i=1;
    cin>>t;
    while(t--)
    {
    long long int n;
    cin>>n;
    while(checkn(n))
    {
    string s=std::to_string(n);
    string temp="";
    temp+=s[s.length()-1];
    int flag=0;
    char a=s[s.length()-1];
    
    for(int i=s.length()-2;i>0;i--)
    {
    if(a>=s[i])
        {
        string gg=temp;
        temp=s[i]+gg;
        a=s[i];
        }
    else
        {
     
        break;
        }
     }
    n-=(stoll(temp)+1);
    }
    
    cout<<"Case #"<<i<<": "<<n<<endl;
    i++;
    }
return 0;
}
