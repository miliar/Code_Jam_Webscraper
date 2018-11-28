#include <iostream>
#include <list>
#include <fstream>
#include <map>


using namespace std;
typedef long long int llint;

map<llint,int> valCount;

llint op(llint k)
{
    while(true)
    {
        map<llint, int>::iterator itBig;
        llint value = 0;
        for(auto it = valCount.begin(); it != valCount.end(); it++)
        {
            if(it->first > value)
            {
                itBig = it;
                value = it->first;
            }
        }
        int theCount = itBig->second;
        if(k <= theCount)
        {
            return value;
        }

        llint left = (value-1) / 2;
        llint right = value / 2;

        valCount.erase(itBig);

        if(left > 0)
        {
            if(!valCount.count(left))
            {
                valCount[left] = theCount;
            }
            else
            {
                valCount[left] += theCount;
            }
        }

        if(right > 0)
        {
            if(left != right && !valCount.count(right))
            {
                valCount[right] = theCount;
            }
            else
            {
                valCount[right] += theCount;
            }
        }



        k -= theCount;
    }
}

int main()
{
    string inname = "C-small-2-attempt1.in";
    string outname = "C-small-2-attempt1.out";
    ifstream infile(inname);
    ofstream outfile(outname);

    int T;
    infile >> T;
    int n,m;
    for(int i = 1; i <= T; i++){
        infile >> n >> m;
        valCount.clear();
        valCount[n] = 1;
        llint res = op(m);
        llint minLR = (res - 1) / 2;
        llint maxLR = res / 2;
        outfile << "Case #" << i <<": " << maxLR << " " << minLR;
        if(i < T)
            outfile << endl;
    }
    infile.close();
    outfile.close();

    return 0;
}
