#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("B-large .in");
    fout.open("B-large-N.txt");
    int T;
    fin >> T;


    for(int y=0;y<T;y++)
    {

        long long n,temp,i=0;

        vector<int> Number,Number1;

        fin >> n;
        temp = n;

        while(temp!=0)
        {

            int t;
            t = temp%10;
            Number.push_back(t);
            temp/=10;
            i++;

        }

        int o=0;
        for(int j=1;j<i;j++)
        {

            if(Number[j] > Number[j-1])
            {

                o=j;
                Number[o]--;

            }

        }

        for(int l=o-1;l>=0;l--)
        {

            Number[l]=9;

        }
        fout << "Case #"<<y+1<<": ";
        if(Number[i-1]!=0)fout << Number[i-1];
        for(int j=i-2;j>=0;j--)
        {

            fout << Number[j];

        }
        fout << endl;

    }



}
