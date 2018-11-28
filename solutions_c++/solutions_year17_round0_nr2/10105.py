#include<iostream.h>
#include<stdio.h>
#include<fstream.h>


int ch=1,t;
int n,nt,rv=0;
int flag=0;

int temp=9;
int chk()
{
    while(nt!=0)
    {
        if(nt%10<=temp)
        { 
            temp=nt%10;
        }
        else
        return 0;
        nt=nt/10;
    }
    return 1;
}

int main()
{  
   ifstream fin("input.txt");
   ofstream fout("output.txt");
   fin>>t;
   while(ch<=t)
   {
       fin>>n;
       nt=n;
       for(nt=n;flag==0;n--)
       {
           nt=n;
           flag=chk();temp=9;
           if(flag==1)
           break;
           
       }
       fout<<"Case #"<<ch<<": "<<n<<"\n";flag=0;
       ch++;
   }return 0;
}