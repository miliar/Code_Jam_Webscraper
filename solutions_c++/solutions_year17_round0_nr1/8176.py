#include <iostream>
#include <fstream>

using namespace std;
string s; int k;
void convert(int st){
    for (int i=0;i<k;i++)
        s[st+i] = (s[st+i]=='+') ? '-': '+';
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("pancake.out");
    int t;
    fin>>t;
    for (int i=0;i<t;i++) {
        int counter=0;
        fin>>s>>k;
        for (int j=0;j<=s.length()-k;j++)
            if (s[j]=='-') {
                convert(j);
                counter++;
            }
        bool cond=true;
        for (int j=s.length()-k+1;j<s.length();j++)
            if (s[j]=='-')
                cond=false;
        fout<<"case #"<<i+1<<": ";
        if (cond) fout<<counter<<endl;
        else fout<<"IMPOSSIBLE"<<endl;

    }
    return 0;
}
