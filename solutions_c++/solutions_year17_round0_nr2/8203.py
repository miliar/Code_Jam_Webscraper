#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t;
    string s;
    ifstream fin("B-large.in");
    ofstream fout("tidy.out");
    fin>>t;
    for (int k=0;k<t;k++){
        fin>>s;
        int i=0;
        while ((i<s.length()-1)&& s[i+1]>=s[i]) i++;
        fout<<"Case #"<<k+1<<": ";
        if (i==s.length()-1 || (s.length()==1)) {fout<<s<<endl; continue;}
        while ((i>0) && (s[i]==s[i-1])) i--;
        if ((!i) && (s[i]==1)) {
            for (int j=0;j<s.length();j++)
                fout<<9;
            fout<<endl;
            continue;
        }
        else{
            for (int j=0;j<i;j++)
                fout<<(char) s[j];
            if (s[i]!='1')
                fout<<(char) (s[i]-1);
            for (int j=i+1;j<s.length();j++) {
                fout<<9;
            }
            fout<<endl;
        }

    }
    return 0;
}
