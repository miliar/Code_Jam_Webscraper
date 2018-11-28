#include <bits/stdc++.h>
#include<cstring>
using namespace std;

string tostring(long long n)
{
    string ret="";
    while(n>0)
    {
        int a=n%10;
        ret+=char(a+'0');
        n/=10;
    }
    reverse(ret.begin(),ret.end());
    return ret;
}


bool istidy(long long n)
{
    string s=tostring(n);
	int i;
	for(i=0;i<s.length()-1;i++)
	{
		if(s[i]>s[i+1])
		return false;
	}
	return true;
}



void rearr(long long &n)
{
    string s=tostring(n);
	int i,j;
	for(i=0;i<s.length()-1;i++)
	{
		if(s[i]>s[i+1])
		{
		    s[i]=char(s[i]-1);
		    for(j=i+1;j<s.length();j++)
            {
                s[j]='9';
            }
            break;
		}
	}

	long long temp=0;
	long long k=1;
	for(i=s.length()-1;i>=0;i--)
    {
        temp+=(s[i]-'0')*k;
        k*=10;
    }
	n=temp;
}

long long lastidy1(long long n)
{
    while(!istidy(n))
    {
        rearr(n);
    }
    return n;
}

int main()
{
    ofstream myfile ("example1.txt");
    ifstream ip ("B-large.txt");
    if (ip.is_open())
    {
      int i=1;
      int t;
      ip>>t;
      if (myfile.is_open())
      {
        while(t--)
        {
            long long n;
            ip>>n;
            myfile<<"Case #"<<i<<": ";
            myfile<<lastidy1(n)<<endl;
            i++;
        }
      }
    }
    return 0;
}
