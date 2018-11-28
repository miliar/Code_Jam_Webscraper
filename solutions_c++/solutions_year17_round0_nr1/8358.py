#include <iostream>
#include <fstream>

using namespace std;

class PancakeStack
{
private:
    bool * theStack;
    int flipperSize;
    int stackSize;
public:
    bool stackUpright();
    int leftMostToFlip();
    PancakeStack(int size, string ss);
    void doAFlip(int startIndex);
    int countFlips();
    void printStack(ostream& out);
};

int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("A-large.in");
    outFile.open("out.dat");

    int T;
    inFile>>T;

    for (int mainLoop=0;mainLoop<T;mainLoop++)
    {
      //  cout<<"Case"<<mainLoop+1<<endl;
        string pStack;
        int flipperSize;

        inFile>>pStack;
        inFile>>flipperSize;

        PancakeStack ss(flipperSize,pStack);
        int f = ss.countFlips();

        //this line is different if f is -1
        outFile<<"Case #"<<mainLoop+1<<": ";
        if (!ss.stackUpright())
            outFile<<"IMPOSSIBLE"<<endl;
        else
            outFile<<f<<endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}

PancakeStack::PancakeStack(int size, string ss)
{
    stackSize = ss.length();
    theStack = new bool[stackSize];

    flipperSize = size;

  //  cout<<"Stack size"<<stackSize<<endl;
    //cout<<"Flipper size"<<flipperSize<<endl;

    for (int k=0;k<stackSize;k++)
    {
        if (ss[k]=='+')
            theStack[k]=1;
        else
            theStack[k]=0;
    }
}

void PancakeStack::doAFlip(int startIndex)
{
    for (int k=startIndex;k<startIndex+flipperSize;k++)
        theStack[k]=!theStack[k];
}

int PancakeStack::countFlips()
{
    int flipLimit = stackSize-flipperSize+1;
    int flips=0;
    bool fail=false;


    while (flips<flipLimit && !stackUpright())
    {
     //   cout<<"Flip limit"<<flipLimit<<endl;
        if (leftMostToFlip()<flipLimit)
        {
       //     cout<<"Flipping from: "<<leftMostToFlip()<<endl;
            doAFlip(leftMostToFlip());
            flips++;
        }
        else
        {
       //     cout<<"Flip not possible"<<endl;
            fail=true;
            return flips;
        }
     //   printStack(cout);
    }

    return flips;
}

void PancakeStack::printStack(ostream& out)
{
    for (int k=0;k<stackSize;k++)
        if (theStack[k]==1)
            out<<"+";
        else
            out<<"-";
    out<<endl;
}

int PancakeStack::leftMostToFlip()
{
    bool found=false;
    int cc=0;
    while (!found)
    {
        if (theStack[cc]==0)
            found=true;
        else
            cc++;
        if (cc>=stackSize)
            return -1;
    }
    return cc;
}
bool PancakeStack::stackUpright()
{
    if (leftMostToFlip()==-1)
        return true;
    else
        return false;
}

