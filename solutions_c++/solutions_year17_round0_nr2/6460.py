#include<iostream>
#include<string>
using namespace std;

string s;
long long int conv(string s)
{
    long long int l=s.length(),x,ans,y,i,d;
    d=1;
    ans=0;
    for(i=l-1;i>=0;i--)
    {
        y=s[i]-48;
        ans+=y*d;
        d=d*10;
    }

    return ans;
}

bool tidy(string s)
{
int i,l=s.length();
for(i=1;i<l;i++)
{
    if(s[i]<s[i-1])
        {return false;}
}
    return true;
}

long long int make_tidy(string s)
{   char nine='9';
    int i,j,k,l=s.length();
    for(i=0;i<l-1;i++)
    {
        if(s[i]>s[i+1])
            break;
    }
    for(j=i+1;j<l;j++)
    {
        s[j]=nine;

    }
        s[i]=s[i]-1;


       for(j=i;j>=0;j--)
        {
            if((s[j]=='0')&&(j-1>=0))
            {s[j]='9';s[j-1]=s[j-1]-1;}
            else if(j-1>=0)
            {
                if(s[j]<s[j-1])
                  {s[j]='9';s[j-1]=s[j-1]-1;}
            }
            else
                break;
        }


    return conv(s);
}
int main()
{

    long int t,n,i,j;
    cin>>t;
    j=1;
    while(t--)
    {
        cin>>s;
        if(tidy(s))
        {
            cout<<"Case #"<<j<<": "<<s<<endl;
        }
        else
        {
            cout<<"Case #"<<j<<": "<<make_tidy(s)<<endl;
        }
        j++;
    }
}
