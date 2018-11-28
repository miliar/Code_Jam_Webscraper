#include<iostream>
#include <fstream>
using namespace std;
char fun(char c)
{

    if(c=='+') c='-';
    else if (c=='-') c='+';
    return c;
}
string firstPass(string str, int k)
{
    for(int i=0;i<k;i++)
        str[i]=fun(str[i]);
 return str;
}

string secondPass(string str, int k)
{

    int len=str.size();
    for(int i=len-1,j=0;j<k && i>-1;i--,j++)
        str[i]=fun(str[i]);

    return str;
}
string processSubstring(string str, int i, int k)
{

    for(int indx=i;indx<i+k;indx++)
        str[indx]=fun(str[indx]);

    return str;
}
int thirdPass(string str, int k)
{
    int len=str.size();
    int cnt=0;
    for(int indx=1;indx+k<len;indx++)
    {
        if(str[indx]=='-')
        {
            cnt++;
            str=processSubstring(str,indx,k);
        }
    }
    for(int i=len-k;i<len;i++)
    if(str[i]=='-') return -1;
    return cnt;
}
int processString(string str, int k)
{

    int ans=0;
    if(str[0]=='-')
    {
        ans++;
        str=firstPass(str,k);
    }
    int len=str.size();
    if(str[len-1]=='-')
    {
        ans++;
        str=secondPass(str,k);
    }
    if(str[0]=='-') return -1;
    int cnt=thirdPass(str,k);
    if(cnt<0) return -1;
    return ans+cnt;
}
/*void printAns(int cnt, int test)
{
    if(cnt<0)
    {
       outfile<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
    }
    else
    {
        outfile<<"Case #"<<test<<": "<<cnt<<endl;
    }
}*/
int main()
{
    int test;
    ifstream infile ("jam1big.in");
    ofstream outfile ("jam1out.txt");
    infile>>test;
    for(int t=0;t<test;t++)
    {
        string str;
        int k;
        infile>>str;
        infile>>k;
        int cnt=processString(str,k);
        //printAns(ans,t,outfile);
        if(cnt<0)
        {
            outfile<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
        }
        else
        {
            outfile<<"Case #"<<t+1<<": "<<cnt<<endl;
        }
    }
    return 0;
}
