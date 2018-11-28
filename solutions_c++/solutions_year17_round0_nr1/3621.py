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
int t,i,j,k,l;
bool b=false;
		string s;
cin>>t;
	repd(i,t)
	{b=false;
	    cin>>s>>k;
	    ans=0;
	    for(j=0;j<s.length()-k+1;j++)
        {

            if(s[j]=='+')
                continue;

            else if(j+k<=s.length())
            {//cout<<j<<" "<<j+k-1<<endl;
                ans++;
                for(l=j;l<j+k;l++)
                {

                    if(s[l]=='+')
                        s[l]='-';
                    else
                        s[l]='+';

                }

            }

        }
        //cout<<"NEW STRING"<<s<<endl;
	    for(j=0;j<s.length();j++)
        {
            if(s[j]=='-')
            {
                ans=-1;
                break;
            }
        }
        if(ans==-1)
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
            else
            cout<<"Case #"<<i<<": "<<ans<<endl;


	}
	// your code goes here
	return 0;
}
