#include<bits/stdc++.h>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("out113.txt");
int main()
{
int t;
int l1;
l1=1;
fin>>t;
while(t--)
{
    string s;
    fin>>s;
    int l=s.length();
char    prev=s[l-1];
int pos;
    for(int i=(l-2);i>=0;i--)
    {
        if(s[i]>prev)
        {
        int k=(i+1);
        do
        {
        k--;
        int val1=int(s[k]);
        if(val1!=48)
        val1--;
        else
        val1=(48+9);
        char c1=val1;
        s[k]=c1;

        //fout<<i<<" "<<val1<<endl;

        }while(s[k]=='9');
        for(int j=k+1;j<l;j++)
        s[j]=char(48+9);
    }
    //fout<<i<<" "<<s[i]<<endl;
    prev=s[i];
    }
    int i;
    for( i=0;i<l;i++)
    {
    if(s[i]!='0')
   break;

    }
    fout<<"Case #"<<l1<<": ";
    l1++;
    for(int j=i;j<l;j++)
    fout<<s[j];
    fout<<endl;
}

}
