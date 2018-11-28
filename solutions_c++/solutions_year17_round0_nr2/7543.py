#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int test;
    ifstream infile ("jam2big.in");
    ofstream outfile ("jam2out.txt");
    infile>>test;
    for(int t=0;t<test;t++)
    {
        string str;
        infile>>str;
        int len=str.size();
        int indx=-1;
        for(int i=0;i<len-1;i++)
        {
            if(str[i]>str[i+1])
            {
                indx=i;

                str[i]--;

                break;

            }

        }

        for(int i=indx;i>0;)
        {
            if(str[i]<str[i-1])
            {

                indx=i-1;

                i=indx;
                str[indx]--;

            }
            else i--;

        }
        outfile<<"Case #"<<t+1<<": ";
        if(str[0]=='0')
        {

            for(int i=1;i<len;i++) outfile<<"9";
            outfile<<endl;

        }
        else if(indx>-1)
        {
            for(int i=indx+1;i<len;i++) str[i]='9';
            outfile<<str<<endl;
        }
        else outfile<<str<<endl;


    }
    return 0;
}
