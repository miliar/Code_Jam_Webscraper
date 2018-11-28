#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream inFile;
    ofstream outFile;
    ofstream debug;

    //inFile.open("in.dat");
    inFile.open("A-large.in");
    outFile.open("out.dat");
    debug.open("debug.dat");

    int T;
    inFile>>T;

    for (int main=0;main<T;main++)
    {
        debug<<"case "<<main+1<<endl;
        int distance;
        int horses;
        inFile>>distance;
        inFile>>horses;
        debug<<distance<<endl;

        double slowest = 0.0;
        for (int k=0;k<horses;k++)
        {
            int start, speed;
            inFile>>start;
            inFile>>speed;
            debug<<start<<'\t'<<speed<<endl;
            long double courseLeft=distance-start;
            debug<<courseLeft<<endl;
            double timeNeeded=courseLeft/speed;
            debug<<timeNeeded<<endl;
            if (timeNeeded>slowest)
                slowest = timeNeeded;
        }

        double cruise = distance/slowest;

        outFile.precision(17);
        outFile<<"Case #"<<main+1<<": "<<cruise;
        outFile<<endl;
        debug<<"Case #"<<main+1<<": "<<cruise;
        debug<<endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
