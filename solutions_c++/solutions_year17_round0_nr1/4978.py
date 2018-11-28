#include<fstream>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;


int solve(string &s, int n)
{  
  int i,j,num=0;
   for(i=0;i<s.size()-n+1;i++)
    {
       if(s[i]=='+') continue;
       for(j=i;j<i+n;j++) 
         { if(s[j]=='+') s[j]='-'; else s[j]='+';}
       num++;
       
    }
   
//cout<<s<<endl;
   for(i=0;i<s.size();i++)
    if(s[i]=='-') return -1;
   
   
   return num;
  
   
}


int main()
{ 
 int n,i,j,c;
  string num;
  int res;
  ofstream output;
  output.open("outputAlarge.txt");
  
  ifstream input;
  input.open("A-large.in");
  input>>n;
  cout<<n<<endl;
 
  for(j=1;j<=n;j++)
  { //input>>s; //cout<<s<<endl;
    input>>num>>c;
         
    res=solve(num,c);
    if(res>=0)
    output<<"Case #"<<j<<": "<<res<<endl; 
    else output<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
   // cout<<j<<endl;

  }
  
 input.close();
 output.close();
//string s="-+-+-";
//cout<<solve(s,4)<<endl;
   return 0;
}
