#include <iostream>
#include<string>
#include<fstream>

using namespace std;

int check(string s)
{
    for(int i=0;i<=s.length()-1;i++)
    {
        if(s[i]=='+')
        {
            continue;
        }
        else{
            return 0;
        }
    }
    return 1;
}

int main()
{
   ifstream fin("A-large.in.txt");
   ofstream fout("f.txt");
   string s;
   int t,i,n;
   int flips;
   fin>>t;

   //cin>>t;
   for(i=1;i<=t;i++)
   {
       flips=0;
fout << "Case #" << i << ": ";

       fin>>s;
       fin>>n;
       //cin>>n;
       for(int j=0;j<=s.length()-n;j++)
       {
         if(s[j]=='-')
         {
             flips++;
            for(int k=j;k<j+n;k++)
    {
        s[k]=(s[k]=='-')?'+':'-';
    }
          // cout<<s<<endl;
          // j=j+n-1;
         }

       }
int c=check(s);
   if(c)
   {
       fout<<flips<<endl;
       //cout<<flips<<endl;
   }
   else{
    fout<<"IMPOSSIBLE"<<endl;
    //cout<<"IMPOSSIBLE"<<endl;
   }
   }


    return 0;
}
