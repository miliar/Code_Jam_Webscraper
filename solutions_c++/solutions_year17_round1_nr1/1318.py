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
freopen("output1.txt","w",stdout);

int t,i,k,j;

cin>>t;
	repd(k,t)
	{
	    int r,c;
	    cin>>r>>c;
	    string s[30];
	    for(i=0;i<r;i++)
            cin>>s[i];
        char ch='a',ch1='a';
        for(i=0;i<r;i++)
        {char ch='a',ch1='a';

            for(j=0;j<c;j++)
            {
                if(s[i][j]=='?' && ch !='a')
                    s[i][j]=ch;
                else if(s[i][j]!='?')
                    ch = s[i][j];
                if(ch1=='a' && s[i][j]!='?')
                ch1=s[i][j];
            }

            if(ch1!='a' && ch1!='?')
            {
                for(j=0;j<c;j++)
            {
                if(s[i][j]=='?')
                    s[i][j]=ch1;
            }
            }
        }
        for(i=0;i<c;i++)
        {char ch='a',ch1='a';
        for(j=0;j<r;j++)
        {
            if(s[j][i]=='?' && ch !='a')
            {
                s[j][i]=ch;
            }
             else if(s[j][i]!='?')
                    ch = s[j][i];
                if(ch1=='a' && s[j][i]!='?')
                ch1=s[j][i];
        }

        if(ch1!='a' && ch1!='?')
            {
                for(j=0;j<r;j++)
            {
                if(s[j][i]=='?')
                    s[j][i]=ch1;
            }
            }

        }


	        cout<<"Case #"<<k<<":"<<endl;
	        for(i=0;i<r;i++)
                cout<<s[i]<<endl;

	}
	// your code goes here
	return 0;
}
