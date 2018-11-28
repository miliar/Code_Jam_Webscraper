#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
void itoa1(char *s,unsigned long long n)
{int i=0;
while(n!=0)
{
s[i]=n%10+'0';
i++;
n/=10;
}char tmp;
for(i=0;i<strlen(s)/2;i++)
{tmp=s[i];
s[i]=s[strlen(s)-1-i];
s[strlen(s)-1-i]=tmp;
}
}
void smaller(char *s,int i)
{
int n=strlen(s);
for(;i<n;i++)
{
s[i]='9';
}
}

void makeitlarge(char *s,int i)
{
if(i==strlen(s)-1)return;
if(s[i]<=s[i+1]) makeitlarge(s,1+i);
else if(i==0||s[i]>s[i-1]) {
s[i]--;
smaller(s,i+1);
}
else {
while(i!=0&&s[i]==s[i-1])
i--;
s[i]--;
smaller(s,i+1);
}

}

unsigned long long atoi1(char*s)
{unsigned long long n=0;
int i=0;
for(;i<strlen(s);i++)
n=n*10+s[i]-'0';
return n;
}

int main()
{int t;
cin>>t;
ofstream myfile;
myfile.open("tidynumbers.txt");
for(int i=0;i<t;i++)
{unsigned long long n;
cin>>n;
char *s=(char*)calloc(sizeof(char),19);
itoa1(s,n);
makeitlarge(s,0);
n=atoi1(s);
myfile<<"Case #"<<i+1<<": "<<n<<"\n";
}
myfile.close();}
