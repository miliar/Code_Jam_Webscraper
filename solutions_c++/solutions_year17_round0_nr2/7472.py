#include<bits\stdc++.h>
#include<iostream>
#include<string>
#include<stdlib.h>

#define ll long long int

using namespace std;
void pichla(string &s,int idx)
{
//	cout<<"\npassed: "<<idx;
	for(int i=idx;i>=0;i--)
	{
//		cout<<"\nDecreasing: "<<s[i]<<"\tin i: "<<i;;
		if(s[i]>'1')
		{ s[i]=s[i]-1;if( s[i]<s[i-1] ){ s[i]='9';continue;		}  return;	}
		else
		{
			if(i==0)
			{ s[i]='0';		}
			else
			{ s[i]='9';	 }
		}
	}
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int t,i,j,k,ctrf,ctre;
    unsigned ll n,res;
    cin>>t;
    for(k=0;k<t;k++)
    {
    cin>>n;
    stringstream ss;
    ss << n;
    string s2 = ss.str();
    ss.str(std::string());
    for(i=0;i<s2.length()-1;++i)
    {

    	if(s2[i]>s2[i+1])
    	{  pichla(s2,i);for(j=i+1;j<s2.length();++j){  s2[j]='9'; };break;	}
	}

    stringstream(s2) >> res;
    cout<<"case #"<<k+1<<": "<<res<<"\n";
    }

	return 0;
}

