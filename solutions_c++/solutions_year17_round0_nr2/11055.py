#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");

    int t,l,i,j,k;
	string s;
	fin>>t;
    for(j=1;j<=t;j++)
	{
	    fin>>s;
	    l=s.length();
	    if(l>1)
        {

            for(i=l-1;i>0;i--)
            {
                if(s[i-1]>s[i])
                {
                	s[i-1]--;
                    for(k=i;k<l;k++)
                        s[k]=9+'0';
                }
            }

            if(s[0]=='0')
            {
                for(i=0;i<l-1;i++)
                {
                    s[i]=s[i+1];
                }
                s[i]=' ';
            }
        }
	    fout<<"Case #"<<j<<": "<<s<<endl;
	}

    fin.close();
    fout.close();
	return 0;
}
