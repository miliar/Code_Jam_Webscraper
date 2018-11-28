#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("B-small-attempt2.in");
    fout.open("B-small-attempt2_out.txt");

    int T;

    fin >> T;

    for(int x=0;x<T;x++)
    {

        vector<int> color;
        vector< vector<int> > data;
        int n,r,o,y,g,b,v;

        fin>>n>>r>>o>>y>>g>>b>>v;

        color.push_back(r);
        color.push_back(int('R'));
        data.push_back(color);
        color.clear();
        color.push_back(b);
        color.push_back(int('B'));
        data.push_back(color);
        color.clear();
        color.push_back(y);
        color.push_back(int('Y'));
        data.push_back(color);
        color.clear();

        sort(data.begin(), data.end());

        fout<<"Case #"<<x+1<<": ";

        if(r>y+b || y>r+b || b>r+y )
            fout<<"IMPOSSIBLE"<<endl;
        else
        {
            while(data[1][0] > data[0][0])
            {
                fout<<char(data[2][1])<<char(data[1][1]);
                data[2][0]--;
                data[1][0]--;
            }

            while(data[2][0] > data[1][0])
            {
                fout<<char(data[2][1])<<char(data[1][1])<<char(data[2][1])<<char(data[0][1]);
                data[2][0] -= 2;
                data[1][0]--;
            }

            while(data[2][0]>0)
            {
                fout<<char(data[2][1])<<char(data[1][1])<<char(data[0][1]);
                data[2][0]--;
            }
            fout<<endl;

        }
        //cout << "Case #"<<y+1<<": "<<ans<<endl;;
    }

}
