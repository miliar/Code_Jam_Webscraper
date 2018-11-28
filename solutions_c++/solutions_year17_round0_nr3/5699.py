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
        int n;
        int ls;
        int rs;

        vector<int> interval;
        vector<int> people;
        fout<<"Case #"<<ii<<": ";
        fin>>n>>k;
        interval.push_back(n+1);
        people.push_back(0);
        people.push_back(n+1);
        for (int i=0;i<k;i++)
        {
            int maxinterval=-1;
            int maxpos=-1;
            for (int j=0;j<i+1;j++)
            {
                if (interval[j]>maxinterval)
                {
                    maxinterval=interval[j];
                    maxpos=j;
                }
            }
                people.insert(people.begin()+maxpos+1,  (people[maxpos]+people[maxpos+1])/2 );
                interval[maxpos]=maxinterval/2;
                interval.insert(interval.begin()+maxpos+1, maxinterval-interval[maxpos] );
            
            ls=people[maxpos+1]-people[maxpos]-1;
            rs=people[maxpos+2]-people[maxpos+1]-1;
        }
        
        
        fout<<max(ls,rs)<<' '<<min(ls,rs);
        fout<<endl;
    }
    return 0;
}