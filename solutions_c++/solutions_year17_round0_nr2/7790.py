#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

string to_string(unsigned long long i)
{
    std::stringstream ss;
    ss << i;
    return ss.str();
}

int main()
{
    ifstream in("tidyin.txt");
    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    ofstream out("tidyout.txt");
    streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    int n;
    cin>>n;
    for(int i=0;i<n;++i)
    {
        unsigned long long k;
        cin>>k;
        string ks=to_string(k);
        if(k>=10)
        {
            int j=1;
            while(j<ks.size() and (ks[j]-'0')>=(ks[j-1]-'0')) j++;
            if(j<ks.size())
            {
                j--;
                while(j>0 and (ks[j]-'0')==(ks[j-1]-'0')) j--;
                k=(unsigned long long)(k/pow(10,ks.size()-j-1))*pow(10,ks.size()-j-1);
                k--;
            }
        }
        cout<<"Case #"<<i+1<<": "<<k<<endl;
    }

    return 0;
}
