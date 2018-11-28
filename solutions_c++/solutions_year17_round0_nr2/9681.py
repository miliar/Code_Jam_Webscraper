#include<iostream>
#include<sstream>

using namespace std;
string tatiana(long long int n)
{
    stringstream ss;
     ss << n;
     string s = ss.str();
     bool check=false;
     if(n>=10){
     for(int i=1;i<s.size();i++)
     {
         char a= s.at(i-1);
         char b=s.at(i);
         if(int(a)>int(b))
         {
             check=true;
         }
     }
     if(check)
     {
        string err ="error";
        return err;
     }
     else{
     return s;
     }
     }
      else{
     return s;
     }
}
int main()
{
    int tc;
    cin>>tc;
    for(int m=1;m<=tc;m++)
    {
     long long int n;
     cin>>n;
     while(n>0)
     {
         string a =tatiana(n);
         if(a=="error")
         {
             n--;
         }
         else
         {
             cout<<"Case #"<<m<<": "<<a<<endl;
             break;
         }
     }
    }
    return 0;
}
