#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{


    ifstream fin;
    ofstream fout;

    fin.open("C-small-1-attempt0.in");
    fout.open("out.txt");

    int t;
    fin >> t;

for(long long int y=0;y<t;y++)
    {
        long long int n, k, mx,ls,rs;
        vector<long long> data;

            fin>>n;
            fin>>k;
        fout<<"\nCase #"<<y+1<<": ";
        data.push_back(n);
        for(int i=0;i<k;i++)
        {
            sort(data.begin(), data.begin()+data.size());
            mx=data.back();
            data.pop_back();
            if(mx%2==0)
            {
                ls=(mx-1)/2;
                rs=(mx-1)/2+1;
                data.push_back(ls);
                data.push_back(rs);
            }
            else
                {
                    ls=rs=mx/2;
                    data.push_back(ls);
                    data.push_back(rs);
                }

 //cout<<"\nls :"<<ls<<" rs:"<<rs;
        }
        fout<<max(ls,rs)<<" "<<min(ls,rs);

    }


}
