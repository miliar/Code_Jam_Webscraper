#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    int n,a=1,count=0;
    string s;
    in>>n;
    while(n--)
    {
        count=0;
        in>>s;
        int k;
        in>>k;
        int l=s.length();
        for(int i=0;i<l-k+1;i++)
        {
            int temp=k;
            if(s[i]=='+')
                continue;
            else
            {
                count++;
                int m=i;
                while(temp--)
                {
                    if(s[m]=='+')
                        s[m++]='-';
                    else
                        s[m++]='+';
                }
            }
        }
        int j=0;
        for(int i=l-k;i<l;i++)
        {
            if(s[i]=='-')
            {
                out<<"Case #"<<a<<":"<<" IMPOSSIBLE"<<endl;
                 j=1;
                 a++;
                 break;
            }
        }
        if(j==0){
            out<<"Case #"<<a++<<":"<<" "<<count<<endl;
        }
    }

}
