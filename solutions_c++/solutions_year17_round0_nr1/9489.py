/*
ID: Jack Avins
PROG: Coin Jam
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int k,count;

int file_num(ifstream &fin)
{
    char ch[5];
    int val=0,i;

    fin>>ch;

    for(i=0;ch[i]!='\n' && ch[i]!=' ' && ch[i]!='\0';i++)
        val = val*10 +(ch[i]-'0');

   return val;
}

void file_char(ifstream &fin,char ch[])
{
    if(!fin.eof())
      fin>>ch;
}

bool check(char *s)
{
    for(int i=0;s[i];i++)
        if(s[i]=='-')
            return false;

    return true;
}

void convert(char *s,int i)
{
    int temp=i+k;
    while(i<temp)
    {
        (s[i]=='+')?(s[i]='-'):(s[i]='+');
        i++;
    }
}


int main()
{
  ifstream fin;
  ofstream fout;

  fin.open("A-large.in");
  fout.open("A-large.out");

  int t=file_num(fin);
  char *s=new char[10000];

//    cout<<t;

  for(int i=0;i<t;i++)
   {
        file_char(fin,s);
        k=file_num(fin);
        count=0;

//        cout<<i<<'\n';

        for(int j=0;s[j+k-1];j++)
        {
            if(s[j]=='-')
            {
                convert(s,j);
                count++;
//                cout<<j<<": "<<s<<' '<<k<<' '<<count<<'\n';
//                cout<<j<<'\n';
            }
        }

        if(check(s))
            fout<<"Case #"<<i+1<<": "<<count<<'\n';
        else
            fout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<'\n';
   }

  fin.close();
  fout.close();

  return 0;
}

