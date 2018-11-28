#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream myfile;
    ofstream outfile;
    myfile.open("A-large.in");
    outfile.open("output.txt");
    string s;
    int t,i,k,c=0,count=1;
    myfile>>t;
    while(t--)
    {

        myfile>>s;
        myfile>>k;
        int l=s.length();
        c=0;
        for(i=0;i<l-k+1;i++)
        {
            if(s[i]=='+')
                continue;
            else
            {
                c++;
                int h=i;
                for(int j=0;j<k;j++)
                {
                    if(s[h]=='-')
                    {
                        s[h++]='+';
                    }
                    else
                    {
                        s[h++]='-';
                    }

                }
            }
        }
        int p=0;
        for(int i=l-k;i<l;i++)
        {
            if(s[i]=='-')
            {
                outfile<<"Case #"<<count++<<":"<<" IMPOSSIBLE"<<endl;
                 p=1;
                 break;
            }
        }
        if(p!=1)
        {
            outfile<<"Case #"<<count++<<": "<<c<<endl;;
        }
    }
}
