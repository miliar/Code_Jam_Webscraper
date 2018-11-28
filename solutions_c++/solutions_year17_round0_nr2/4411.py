#include<bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

int main()
{
   ll t;
   cin>>t;
   for(ll u=1;u<=t;u++)
   {
       string s;
       cin>>s;

           for(int i=s.length()-2;i>=0;i--)
          {
            int x=s[i]-'0';
            int y=s[i+1]-'0';
            if(x>y)
            {
               for(int j=i+1;j<s.length();j++)
               {
                  s[j]='9';
               }
               x=x-1;
               s[i]=(char)(x+48);
             }
           }
        cout<<"Case #"<<u<<": ";
       int mark=0;
       for(int i=0;i<s.length();i++)
       {
           if(s[i]=='0')
           {
               mark++;
           }
           else
           {
               break;
           }
       }
       for(int i=mark;i<s.length();i++)
       {
           cout<<s[i];
       }
       cout<<endl;
     }
    return 0;
}
