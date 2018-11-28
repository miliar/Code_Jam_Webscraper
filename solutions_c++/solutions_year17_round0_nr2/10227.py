#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool wayToSort(int i, int j) { return i > j; }
bool isTidy(int N)
{

    int i = 0; // the array index

    vector<int> bots,bots2;

     while (N) { // loop till there's nothing left
        bots.push_back(N % 10); // assign the last digit
        N /= 10; // "right shift" the number
    }

    bots2=bots;
    sort(bots.begin(), bots.end(),wayToSort);
    /*for(int i=0;i<bots.size();i++)
    {
        cout << bots.at(i) <<endl;
    }

     for(int i=0;i<bots2.size();i++)
    {
        cout << bots2.at(i) <<endl;
    }*/

    if(bots2==bots) return true;
    return false;




}
int main(int argc, char* argv[]){



    //freopen("probb.in","r",stdin);
    int T, N;
    int d=0;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cin >> N;
        for(int j=1;j<=N;j++)
        {
            if(isTidy(j)) d=j;
        }

        cout << "Case #"<<i+1<<": "<<d<<endl;

    }
    return 0;
}
