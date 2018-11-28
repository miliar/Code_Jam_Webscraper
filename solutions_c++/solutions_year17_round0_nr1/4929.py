#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("fname2.in", ios::in);
    fout.open("output.txt", ios::out);
    int t;
    fin>>t;
    int casecount = 0;
    while(t--)
    {
        casecount++;
        string s;
        int k;
        fin>>s>>k;

        int flips = 0;
        bool flag = true;
        for(int i=0; s[i]!='\0'; i++)
        {
            if(s[i] == '+')
                continue;

            for(int j=0; j<k; j++)
            {
                if((i+j) >= s.length())
                {
                    flag = false;
                    break;
                }
                if(s[i+j] == '+')
                    s[i+j] = '-';
                else
                    s[i+j] = '+';
            }
            if(flag == false)
                break;
            flips++;
        }
        if(flag == false)
            fout<<"Case #"<<casecount<<": IMPOSSIBLE"<<endl;
        else
            fout<<"Case #"<<casecount<<": "<<flips<<endl;
    }

        fin.close();
        fout.close();
}
