#include <fstream>
#include <iostream>
using namespace std;

int main() {
    fstream fin,fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
	int t;
	fin>>t;
	for(int i=1;i<=t;i++)
	{
	    string s;
	    fin>>s;
	    string ans;
	    if(s.size()==1)
            ans=s;
        else
        {
            for(int j=s.size()-1;j>0;j--)
            {
                if(s[j]<s[j-1])
                {
                    s[j-1]=s[j-1]-1;
                    for(int k=j;k<s.size();k++)
                        s[k]='9';
                }
            }
            int j=0;
            while(s[j]=='0')j++;
            ans=s.substr(j);
        }
	    fout<<"Case #"<<i<<": ";
	    fout<<ans<<endl;

	}
	return 0;
}
