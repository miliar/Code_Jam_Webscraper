#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("A-Large.in");
    fout.open("A-Large-N.txt");

    int T;

    fin >> T;

    for(int y=0;y<T;y++)
    {

        string S;
        int k,sz,c=0;

        fin >> S;
        fin >> k;

        sz = S.length();

        int j=0;
        while(j < sz)
        {

            while(S[j] != '-' && j<sz)
                j++;
            //cout << S[j]<<endl;
            if(S[j]!='-')break;

           // cout << j+k << " "<<sz<<endl;

            if(j+k <= sz)
            {

                for(int l=j;l<j+k;l++)
                {

                    if(S[l]=='-')S[l]='+';
                    else S[l]='-';

                }
                c++;

                //cout << c << endl;

            }
            else
            {
                c=-1;
                break;

            }

        }

        if(c==-1)fout <<"Case #"<<y+1<<": "<<"IMPOSSIBLE"<<endl;
        else fout << "Case #"<<y+1<<": "<<c<<endl;

    }

}
