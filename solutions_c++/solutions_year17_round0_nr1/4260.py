#include<iostream>
#include<fstream>
#include<string>
using namespace std;
ifstream in("A-large.in");
ofstream out("A-large.out");
string s;
int k;
void flip(int p)
{
    for(int i=0; i<k; i++)
    {
        if(s[p+i]=='+')
            s[p+i]='-';
        else if(s[p+i]=='-')
            s[p+i]='+';
    }
}
bool check(){
    for(int i=0; i<s.size(); i++)
        if(s[i]!='+')
            return false;
    return true;
}
int main()
{
    int t;
    in>>t;
    for(int c=1; c<=t; c++)
    {
        int ans=0;
        in>>s>>k;
        for(int i=0; i<s.size()-k+1; i++)
        if(s[i]=='-'){
                flip(i);
                ans++;
        }
        out<<"Case #"<<c<<": ";
        if(!check())
            out<<"IMPOSSIBLE";
        else
            out<<ans;
        out<<endl;
    }
}
