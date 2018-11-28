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
        fin>>k;
        int n=ss.size();
//        cout<<ss;
        vector<int> arr;
        for (int i=0;i<n;i++)
        {
            if (ss[i]=='-')
              arr.push_back(0);
            else
              arr.push_back(1);
        }
        
        total=0;

        for (int i=0;i<n-k+1;i++)
        {
            if (arr[i]==0)
            {
                total++;
                for (int j=i;j<i+k;j++)
                    arr[j]=1-arr[j];
            }
        }
        bool solution=true;
        for (int i=0;i<n;i++)
        {
            solution&=(arr[i]==1);
        }
        if (solution)
            fout<<total;
        else
            fout<<"IMPOSSIBLE";
        fout<<endl;
        
    }
    return 0;
}