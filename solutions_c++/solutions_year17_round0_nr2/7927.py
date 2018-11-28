#include <bits/stdc++.h>
using namespace std;
string left(string s1)
{
    for(int i=s1.size()-1; i>0; i--)
    {
        if(s1[i]<s1[i-1])
        {
            s1[i]='9';
            s1[i-1]=s1[i-1]-1;
        }
    }
    return s1;
}
string right(string s1)
{
    for(int i=0; i<s1.size(); i++) s1[i]='9';
    return s1;
}
string Sol(string number)
{
    int aux;
    string s1;
    string s2;
    for(int i=0; i<number.size()-1; i++)
    {
        if(number[i]>number[i+1])
        {
            int aux=(number[i]-'0')-1;
            char n=(char)(aux+'0');
            s1=left(number.substr(0,i)+n);
            s2=right(number.substr(i+1,number.size()));
            number=s1+s2;
        }
    }
    return number[0]=='0'?number.substr(1,number.size()):number;
}
int main()
{
    int cases;
    string number;
    cin>>cases;
    for(int i=1; i<=cases; i++)
    {
        cin>>number;
        cout<<"Case #"<<i<<": "<<Sol(number)<<endl;
    }
    return 0;
}