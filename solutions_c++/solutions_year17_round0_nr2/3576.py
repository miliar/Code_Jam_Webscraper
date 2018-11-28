#include <bits/stdc++.h>
#define mod 1000000007
#define mp make_pair
#define pb push_back
#define ll long long
#define rep(i,n) for(i=0;i<n;i++)
#define repd(i,n) for(i=1;i<=n;i++)
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pi 3.14159265358979323846264
using namespace std;



int main() {
	freopen("abc.in","r",stdin);
freopen("output.txt","w",stdout);
		long long int ans=0;
int t,i,j,k,l,last9;
bool b=false;
		string s,s1,s3;
cin>>t;
	repd(i,t)
	{
	    cin>>s;
	    s3=s;

	    s1.clear();
	    int len=s.length();
	    bool gto=false;
	    for(j=0;j<s.length();j++)
        {
            if(s[j]-'0'>1)
              {
               gto=true;
              }
            if(s[j]=='0' and gto ==false)
            {

                len = s.length()-1;
            }

        }
        if(s.length()==1)
            s1=s;

	    else if(len == s.length()-1 && len>0)
        {//cout<<"GHIS"<<endl;

            for(j=0;j<len;j++)
                s1.push_back('9');
        }
        else
        {last9 = s.length()+5;

char last='a';
            b=false;
             for(j=1;j<s.length();j++)
             {
                 if(s[j]==s[j-1] && last=='a' )
                 {last9=j-1;
                 last = s[j-1];
                 }
                 else if(s[j]<s[j-1])
                 {b=true;
                     break;
                 }
                 else if(s[j]>s[j-1])
                 {
                  last = 'a';
                  last9=j;
                  }
             }
             int x;
             if(b==true)
             {
                 x = min(last9,j-1);
             }
             for(l=0;l<=x-1;l++)
                s1.push_back(s[l]);
                s1.push_back(s[x]-1);
             for(l=x+1;l<s.length();l++)
                s1.push_back('9');
        }
        sort(s3.begin(),s3.end());
        if(s3==s)
            s1 = s;

	        cout<<"Case #"<<i<<": "<<s1<<endl;


	}
	// your code goes here
	return 0;
}
