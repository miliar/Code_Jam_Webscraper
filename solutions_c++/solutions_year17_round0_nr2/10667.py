#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
    int t,count=1;
    bool gotIt=false;
    ifstream myfile;
    ofstream ans;
    myfile.open("B-small-attempt4.in.txt");
    ans.open("Tidyanswer.txt");
    myfile >> t;
    while(t--)
    {
        unsigned long long int n,temp;
        myfile >> n;
        //ans<<n<<endl;
        while(!gotIt )
        {

            vector<short>num;
            temp = n;
            while(temp)
            {
                num.push_back(temp%10);
                temp/=10;
            }
            sort(num.begin(),num.end());
            for (int i = 0; i < num.size(); ++i)
            {
                temp*=10;
                temp+=num[i];
            }
            if(temp == n)
            {
                ans<<"Case #"<<count++<<": "<<n<<endl;
                gotIt=true;
            }
            n--;
            num.clear();
        }
        gotIt=false;
    }
    myfile.close();

    return 0;
}
