#include <iostream>
#include <fstream>
#include <set>
#include <math.h>
#include <vector>

using namespace std;

bool getanswer;
int fretraget[26];
int currentfretraget[26];
bool toobig;
int fre[10][26]={0};
string letter[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
ifstream fin("input");
ofstream fout("output");



bool check(string ss)
{
    int n=ss.size();
    for (int i=0;i<n-1;i++)
        if (ss[i]>ss[i+1])
            return false;
    return true;
}
int main()
{
    int inputnumber,ii,n,N,J,countcopy;
    long long count;
    long long div;
    long long divs[11];
    string ss;
    int total=0;
    fin>>inputnumber;
    
    
    for (int ii=1;ii<=inputnumber;ii++)
    {
        int k;
        fout<<"Case #"<<ii<<": ";
        fin>>ss;
        int n=ss.size();
        
        while (true)
        {
            if (check(ss))
            {
                ss.erase(0, min(ss.find_first_not_of('0'), ss.size()-1));
                fout<<ss;
                fout<<endl;
                break;
            }
            for (int i=0;i<n-1;i++)
                if (ss[i]>ss[i+1])
                {
                    ss[i]--;
                    for (int j=i+1;j<n;j++)
                        ss[j]='9';
                    break;
                }
        }
    }
    return 0;
}