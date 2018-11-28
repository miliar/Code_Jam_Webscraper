#include <iostream>
#include <fstream>

using namespace std;

bool checkAllCakes(string arr, int size)
{
    int j = 0;
    while(j<size)
    {
        if(arr[j] != '+')
            break;
        j++;
    }
    if(j == size)
        return true;
    else
        return false;
}
void flipping(string &arr, int k, int fineIndex)
{
    for(int j = 0; j<k; j++)
    {
        int index = fineIndex+1+j;

        if(arr[index] == '-')
            arr[index] = '+';
        else
            arr[index] = '-';
    }
}
bool flipNow(string &arr, int k, int i, int fineIndex, int strLength)
{
    if(fineIndex+1 < strLength && fineIndex+1+k < strLength)
    {
        flipping(arr, k, fineIndex);
        return true;
    }
    else
    {

    }
    return false;
}

int flip(string &arr, int k, int i, int fineIndex, int strLength, int &count)
{
    if(arr[i] == '+' && fineIndex == i-1)
    {
        fineIndex = i;
        //cout<<"fine: "<<fineIndex<<endl;
    }
    else
    {
        //cout<<"Case before: "<<arr<<endl;
        bool isFlipped = flipNow(arr, k, i, fineIndex, strLength);
        //cout<<"Case after: "<<arr<<endl;
        if(isFlipped)
        {
            count++;
            fineIndex++;
        }


    }
    return fineIndex;
}

int main()
{
    ifstream infile("A-large.in");
    ofstream myfile;
    myfile.open ("A-large.out");

    int total;
    infile >> total;
    int caseNo = 0;
    while(++caseNo<=total)
    {
        string str;
        int k;
        infile >> str >>k;

        int i=0;
        int strSize = str.size();
        int fineIndex = -1;
        int count = 0;

        while(i<strSize)
        {
            fineIndex = flip(str, k, i, fineIndex, strSize, count);
            i++;
        }

        //cout<<"final: "<<str<<endl;

        if(checkAllCakes(str, strSize))
        {
            //cout<<"matched"<<endl;
            myfile<<"Case #"<<caseNo<<": "<<count<<endl;
        }
        else
        {
            flipping(str, k, strSize-1-k);
            count++;
            //cout<<"finally: "<<str<<endl;
            if(checkAllCakes(str, strSize))
            {
                //cout<<"finally matched"<<endl;
                myfile<<"Case #"<<caseNo<<": "<<count<<endl;
            }
            else
                myfile<<"Case #"<<caseNo<<": IMPOSSIBLE"<<endl;
        }
    }


    return 0;
}
