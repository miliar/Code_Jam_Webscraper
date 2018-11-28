#include <iostream>
#include<bits/stdc++.h>
using namespace std;
vector<int> j;
   int oo;
   int hh=1;
    ifstream fin("B-large.in");
    ofstream fout("output_file.out");
void countt(string p)
{
 for(int i=0;i<p.size();i++)
    {
        j.push_back(p[i]-'0');




    }




}
void makeit(int y)
{
    for(int i=y;i<j.size();i++)
    {
        j[i]=9;
    }



}
void pp()
{
fout<<"Case #"<<hh<<": ";
    for(int i=0;i<j.size();i++)
    {

        fout<<j[i];

    }
fout<<"\n";
hh++;
}
int checkk()
{
    for(int i=0;i<j.size()-1;i++)
    {
        if(j[i]>j[i+1])
        return 0;


    }


pp();
    return 1;
}
int main()
{


    fin>>oo;
    while(oo--)
    {
        j.clear();
    string p;
    long long k;
    fin>>p;
    if(p.size()==1){
            fout<<"Case #"<<hh<<": ";
        fout<<p<<"\n";
        hh++;
     continue;
    }
    countt(p);
    int i=1,ll=0;
    while(1)
    {ll=0;
        if(checkk())
        {
            break;
        }
        if(j[j.size()-i]-j[j.size()-i-1]==0)
        {
            i++;
            continue;
        }
         if(j[j.size()-i]-j[j.size()-i-1]>0)
        {
            if(checkk())
            break;
            else
                i++;
        }
         if(j[j.size()-i]-j[j.size()-i-1]<0)
        {

            j[j.size()-i-1]--;
            if( j[j.size()-i-1]==0&& j.size()-i-1==0)
            {
                j.erase(j.begin());
                ll=1;
            }
            makeit(j.size()-i);
if(ll)
    i=1;


        }
    }




    }
    return 0;
}
