
#include <iostream>
#include<fstream>
#include<string>

using namespace std;
typedef long long ll;
string modify(string s)
{

    int l=s.length();
        int i=l-1;

    while(s[i]=='0')
    {
        s[i]='9';
        i--;
    }
    s[i]=(int)s[i]-1;
    if(s[0]=='0')
       {
          s=s.substr(1,s.length()-1) ;
       }
   return s;
}
int check(string s)
{

    int l=s.length();
    for(int i=l-1;i>0;i--)
    {

        if((int)s[i]>=(int)s[i-1])
        {
        if(i==1)
        {

            return 1;
        }
        }
        else{
            return 0;
        }

    }
}
int main()
{ifstream fin("B-small-attempt0.in-1.txt");
ofstream fout("B.out.txt");
    int t;
    fin>>t;
  //  cin>>t;
string s;
    for(int i=0;i<t;i++)
    {
        fout << "Case #" << i+1 << ": ";
    //cout << "Case #" << i+1 << ": ";
        fin>>s;//cin>>s;
        int f=0;
        if(s.length()==1)
        {
            fout<<s<<endl;
            continue;
        }
        while(s.length()>1)
        {
f=check(s);
if(f==0)
{

   s= modify(s);
  //  check(s);
}
else if(f==1)
{fout<<s<<endl;
    //cout<<s<<endl;
    break;
}}
    }
return 0;
}
