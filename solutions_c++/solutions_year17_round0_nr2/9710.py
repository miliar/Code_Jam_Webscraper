#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

#define fre freopen("0.in","r",stdin),freopen("0.out","w",stdout)
int main()
{
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small-attempt3.out", "w", stdout);
unsigned long long  score,pos;

int test=0,t;
cin >> t;
    while (t--)
    {
        test++;
        cin>>score;
string s=to_string(score);
if(s.length()==1 || is_sorted(s.begin(),s.end()))
cout << "Case #" << test << ": " << s << "\n";
else
{
for(int i=0;i<s.length();i++){ 
if(s[i]>=s[i+1])
{
s[i]=s[i]-1;
pos=i;
break;
}
}

for(int i=pos+1;i<s.length();i++)
s[i]='9';

if(s[0]=='0')
s.erase(0,1);

cout << "Case #" << test << ": " << s << "\n";
}
s.clear();
}
}   
