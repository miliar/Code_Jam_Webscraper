#include<string.h>
#include<iostream.h>
#include<stdio.h>
#include<fstream.h>


int ch=1,k; char s[1000];
int n;int temp;
int numflips=0;
int len;


void flip(int pos)
{
    if(s[pos]==45)
        s[pos]=43;
    else if(s[pos]==43)
        s[pos]=45;
}
int mystrlen()
{
    int i;
    for(i=1;s[i]!='\0';i++);
    return i;
    
}

int chk()
{
    for(int i=0;i<=len;i++)
    {
        if(s[i]==45)
        return 0;
    }
    return 1;
}

int po=0;
int main()
{  ifstream fin("input.txt");
   ofstream fout("output.txt");
   
   fin>>n;
   while(ch<=n)
   {
       fin>>s; fin>>k;len=mystrlen();
       for(int i=0;i<len&&i+k<=len;i++)
       {
           temp=i;
           
           if(s[i]==45)
           {
               numflips++;
               for(int p=1;p<=k;p++)
               {
                   flip(temp);temp++;
               }
           }
       }
       int c=chk();
       if(c==1)
       {
           fout<<"Case #"<<ch<<": "<<numflips<<"\n";
       }
       else
       {
           fout<<"Case #"<<ch<<": IMPOSSIBLE\n";
       }
       //cout<<s<<" "<<numflips<<"\n";
       ch++;numflips=0;
   }return 0;
}