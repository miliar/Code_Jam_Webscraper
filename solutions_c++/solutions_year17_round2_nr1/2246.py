//Author @ NIRAV ALPESH SHAH
//Mail ID shahniravalpesh@gmail.com

#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<math.h>

using namespace std;

int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("A-large.in");
    fout.open("A-large_ans_Nirav.txt");

    long long T;

    fin >> T;

    for(int y=0;y<T;y++)
    {

        long long int d,k;
        double n,s,m = 0,ans;

        fin>>d>>n;
        //cout << "Hi"<<endl;
        for(long long int j=0; j<n; j++)
        {
            fin>>k>>s;
            m = max(m, (d-k)/s);
        }

        ans = floor(1000000 * (d/m) ) / 1000000 ;
        fout<<"Case #"<<y+1<<": "<<fixed<<ans<<endl;
    }

}
