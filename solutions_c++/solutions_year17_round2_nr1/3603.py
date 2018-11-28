#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    ifstream fin;
    int times;
    fin.open("input.in");
    if(fin.is_open())
    {
        fin>>times;
        for(int x=0;x<times;x++)
        {
            int horses;
            double maxkm,horpos,horspd,bestTime=0,tmp;
            fin>>maxkm>>horses;
            for(int i=0;i<horses;i++)
            {
                fin>>horpos>>horspd;
                tmp=maxkm-horpos;
                tmp=tmp/horspd;
                if(tmp>bestTime)
                    bestTime=tmp;
            }
            cout<<"Case #"<<x+1<<": "<<fixed<<maxkm/bestTime<<endl;
        }
    }
    fin.close();
    return 0;
}
