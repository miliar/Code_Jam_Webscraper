#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

bool allPlus (string pcs)
{
int length=pcs.length();
    for (int i=0;i<length;i++)
    {
        if (pcs[i]!='+')
            return false;
    }
     return true;
}

inline void flip (string &pcs,int index,int n)
{
int i=0;
    while (i<n)
    {
        if(pcs[index]=='+')
        pcs[index]='-';
       else pcs[index]='+';
       index++;
       i++;
    }
}

bool flipPancakes(string &pcs,int n,int &res)
{
 int length=pcs.length();
 for (int i=0;i<length;i++)
 {

    if (allPlus(pcs))
    {
        res=i;
        return true;
    }
    int j=0;
    while (pcs[j]!='-')
    {
        j++;
    }

    if (j>length-n)
        return false;
    flip(pcs,j,n);

 }
}


int main()
{
    ifstream myfile;
    ofstream file;
    file.open("result.txt");
    myfile.open("A-large.txt");
    if (myfile.is_open())
 {
    int n;
   myfile>>n;
   string pancakes;
   int num;
   int result=0;
   for (int i=0;i<n;i++)
   {
       myfile>>pancakes>>num;
       if (flipPancakes(pancakes,num,result))
      file<<"Case #"<<i+1<<": "<<result<<endl;
      else
        file<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
   }
   return 0;
}
else
    return -1;
}

inline void flip (string &pcs,int index,int n)
{
int i=0;
    while (i<n)
    {
        if(pcs[index]=='+')
        pcs[index]='-';
       else pcs[index]='+';
       index++;
       i++;
    }
}

bool flipPancakes(string &pcs,int n,int &res)
{
 int length=pcs.length();
 for (int i=0;i<length;i++)
 {

    if (allPlus(pcs))
    {
        res=i;
        return true;
    }
    int j=0;
    while (pcs[j]!='-')
    {
        j++;
    }

    if (j>length-n)
        return false;
    flip(pcs,j,n);

 }
}


int main()
{
    ifstream myfile;
    ofstream file;
    file.open("result.txt");
    myfile.open("first.txt");
    if (myfile.is_open())
 {
    int n;
   myfile>>n;
   string pancakes;
   int num;
   int result=0;
   for (int i=0;i<n;i++)
   {
       myfile>>pancakes>>num;
       if (flipPancakes(pancakes,num,result))
      file<<"Case #"<<i+1<<": "<<result<<endl;
      else
        file<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
   }
   return 0;
}
else
    return -1;
}
