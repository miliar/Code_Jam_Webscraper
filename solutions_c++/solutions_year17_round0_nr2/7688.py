/*###########################################################################
				Tidy Number
############################################################################*/
#include "bits/stdc++.h"
#define ll long long
#define lld long long int
#define ulld unsigned long long int
#define u_ unsigned
#define ui unsigned int
#define mod 1000000007
#define pi 3.14159265

using namespace std;

bool isTidy(string s)
{
	bool tid = true;
	for (int i = 0; i < s.size()-1; ++i)
	{
		// cout<<s[i]-s[i+1]<<endl;
		if(s[i]-s[i+1]<=0)
			continue;
		else
		{
			tid=false;
			break;
		}
	}
	return tid;
}
void showstr(string s)
{
    cout<<s<<endl;
}


string conv(string s)
{
    if(isTidy(s))
        return s;
    else{
        for(int i=0; i<s.size(); ++i)
        {
            if(s[i]>s[i+1] )
            {
                s[i]=(s[i]=='0'?'9':s[i]-1);
                i++;
                while(i<s.size())
                {
                    s[i]='9';
                    i++;
                }
            }
        }
    return s;
    }
	//return s;
}
string remO(string s)
{
    string st=s;
    if(s[0]=='0'){
    for(int i=0, j=1; i<s.size()-1; ++i, ++j)
    {
        s[i]=s[j];
    }
    s[s.size()-1]=' ';
    }
    return s;
}

int main(int argc, char const *argv[])
{
	lld t;
	int casen=1;
	scanf("%lld",&t);
	while(t--){
		string s;
		cin>>s;
		while(!isTidy(s))
            s=conv(s);
		s=remO(s);
		//printf("Case #%d: %s"casen,s);
		cout<<"Case #"<<casen<<": ";
		cout<<s<<endl;
		casen++;
	}

	return 0;
}
