#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int t=0;
string core(string s){
int k=s.length();
t=0;
for(int i =0;i<k-1;i++)
{if(s[i]>s[i+1]&&t==0)
{s[i]=s[i]-1;
//cout<<(s[i]-'0')<<" ";
t=1;}
if(t==1)
s[i+1]='9';}
return s;
}

int main()
{freopen("gcode_input2.in","r",stdin);
freopen("gcode_output.out","w",stdout);
int q,w=1;
cin>>q;
while(q--){
string s;
cin>>s;
int k =s.length()-1;
while(k--)
{
    s=core(s);
}cout<<"Case #"<<w++<<": ";
if(s[0]=='0')
    cout<<s.substr(1,k)<<endl;
else
cout<<s<<endl;
}
return 0;}
