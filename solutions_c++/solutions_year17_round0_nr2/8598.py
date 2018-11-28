#include<iostream>
#include<fstream>
#include<string>
using namespace std;
string sub(string src1,string src2)
{
    int len1,len2;
    len1=src1.length();
    len2=src2.length();
    string filler(len1-len2,'0');
    src2=filler+src2;
    string res="";
    int carry =0;
    int s1,s2,d,i;
    for(i=0;i<len1;i++)
    {
        s1=src1[len1-1-i]-'0';
        s2=src2[len1-1-i]-'0';
        d=s1-s2-carry;
        if(d<0)
        {
            d+=10;
            carry=1;
        }
        else
        {
            carry=0;
        }
        res=char(d+'0')+res;
    }
    return res;
}
int main()
{
    int T,k;
     ifstream my;
        my.open("b.txt");
        ofstream myf;
        myf.open("small_output7.txt");
    string S;
        my>>T;
    for(int i=1;i<=T;i++)
    {
        my>>S;
            while(1==1)
            {
                bool x=0;
                int k=S.length();
               for(int j=k-1;j>=1;j--)
               {
                       if(S[j]<S[j-1])
                       {
                           for(int l=k-1;l>=j;l--)
                           {
                           S.replace(l,1,"9");
                           }
                           string S1=S.substr(0,j);
                           S1=sub(S1,"1");
                           S.replace(0,j,S1);
                           x++;
                       }
               }
               while(S[0]=='0')
               {
                   S=S.substr(1);
               }
               if(x==0)
               {
                   myf<<"Case #"<<i<<": "<<S<<endl;
                   break;
               }
            }
    }
    return 0;
}


