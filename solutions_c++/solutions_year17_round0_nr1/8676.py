#include<iostream>
#include<string>
#include<fstream>

using namespace std;

string in;
int k, c;

void flip(int l)
{
    c++;
    for(int i=0; i<k; i++)
    {
        //cout<<in[i+l]<<" ";

        if(in[i+l] == '+')
            in[i+l] = '-';

        else
            in[i+l] = '+';
    }
    //cout<<endl;

   // cout<<in<<endl;
}

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("in1.in");
    fout.open("out1.txt");

    int t;

    fin>>t;

    int z=0;

    while(z<t && ++z)
    {
        c = 0;

        fin>>in>>k;

        int l = in.size();

        string out = "";

        for(int i=0; i<l; i++)
            out += '+';

        int i=0;

        while(1)
        {
            while(in[i] != '-' && i<=l-k)
            {
                //cout<<in[i]<<endl;
                i++;
            }

            //cout<<i<<endl;

            if(i > l-k)
                break;

            //cout<<i<<endl;

            flip(i);
            i++;

        }

        fout<<"Case #"<<z<<": ";

        if(in == out)
            fout<<c;

        else
            fout<<"IMPOSSIBLE";

        fout<<endl;

    }
}
