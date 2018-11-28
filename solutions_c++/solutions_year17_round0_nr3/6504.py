#include <iostream>
#include <fstream>

using namespace std;

class Bathroom
{
private:
    bool * stalls;
    int minLsRs(int s);
    int maxLsRs(int s);
    int getLs(int s);
    int getRs(int s);
public:
    int nrOfStalls;
    Bathroom(int sz);
    void occupy(int ind);
    void printBRoom(ostream& out);
    int * findBestStall();
};

int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("C-small-1-attempt0.in");
    outFile.open("out.dat");

    int T;
    inFile>>T;

    for (int mainLoop=0;mainLoop<T;mainLoop++)
    {
        cout<<"case "<<mainLoop+1<<endl;
        int N;
        int K;
        inFile>>N;
        inFile>>K;

        Bathroom b(N);
        int * bestStall;
        bestStall = new int[3];
        for (int k=0;k<K;k++)
        {
            bestStall = b.findBestStall();
            b.occupy(bestStall[2]);
            //b.printBRoom(cout);
        }
        outFile<<"Case #"<<mainLoop+1<<": ";
        outFile<<bestStall[1]<<" "<<bestStall[0]<<endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}

int Bathroom::getLs(int s)
{
    bool ocFound=false;
    int cur=s-1;
    int ls=0;
    while (!ocFound && cur>=0)
    {
        if (stalls[cur]==0)
        {
            ls++;
            cur--;
        }
        else
            ocFound=true;
    }

    return ls;
}

int Bathroom::getRs(int s)
{
    bool ocFound=false;
    int cur=s+1;
    int rs=0;
    while (!ocFound && cur<nrOfStalls)
    {
        if (stalls[cur]==0)
        {
            rs++;
            cur++;
        }
        else
            ocFound=true;
    }

    return rs;
}

Bathroom::Bathroom(int sz)
{
    stalls = new bool[sz];
    nrOfStalls=sz;
    for (int k=0;k<sz;k++)
        stalls[k]=0;
}

int Bathroom::minLsRs(int s)
{
    if (stalls[s]==true)
        return -1;
    int l = getLs(s);
    int r = getRs(s);

    if (l<r)
        return l;
    else
        return r;
}

int Bathroom::maxLsRs(int s)
{
    if (stalls[s]==true)
        return -1;
    int l = getLs(s);
    int r = getRs(s);

    if (l>r)
        return l;
    else
        return r;
}

void Bathroom::printBRoom(ostream& out)
{
    for (int k=0;k<nrOfStalls;k++)
        if (stalls[k]==true)
            out<<"o";
        else
            out<<"-";
    out<<endl;
}
void Bathroom::occupy(int ind)
{
    stalls[ind]=true;
}

int * Bathroom::findBestStall()
{
    int * curBest;
    curBest = new int[3]; //0 minLsRs 1 maxLsRs 2 stall
    curBest[0]=-1;
    curBest[1]=-1;
    curBest[2]=-1;

    for (int k=nrOfStalls-1;k>=0;k--)
        {
            int mn = minLsRs(k);
            int mx = maxLsRs(k);

            if (mn>curBest[0])
            {
                curBest[0]=mn;
                curBest[1]=mx;
                curBest[2]=k;
            }
            else if (mn==curBest[0])
                if (mx>=curBest[1])
                {
                    curBest[0]=mn;
                    curBest[1]=mx;
                    curBest[2]=k;
                }
        }
    return curBest;
}
