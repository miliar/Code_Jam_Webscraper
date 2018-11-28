#include<bits/stdc++.h>
using namespace std;
int main()
{
     freopen( "input.txt", "r", stdin );
	 freopen( "output.txt", "w", stdout );
	 int t,z=1;
	 cin>>t;
	 while(t--)
     {
         string s;
         int k,p=0,flips=0,count=0,j,i;
         cin>>s;
         cin>>k;
         cout<<"Case #"<<z<<":"<<" ";
         for(i=0;i<s.length();i++)
         {
             if(s[i]=='+')
                p++;
         }
         if(p==s.length())
            cout<<0<<endl;
         else
         {
             for(i=0;i<=s.length()-k;i++)
             {
                 if(s[i]=='+')
                    continue;
                 else
                 {
                     flips++;
                     for(j=i;j<i+k;j++)
                     {
                         if(s[j]=='+')
                            s[j]='-';
                         else
                            s[j]='+';
                     }
                 }
             }
             for(i=0;i<s.length();i++)
             {
                 if(s[i]=='+')
                    count++;
             }
             if(count==s.length())
                cout<<flips<<endl;
             else
                cout<<"IMPOSSIBLE"<<endl;
         }
         z++;
     }
}
