#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>

using namespace std;

long findmax(vector<long> Sub)
{

    long ma = 0;
    for(long i=0;i<Sub.size();i++)
    {

        if(Sub[i]>Sub[ma])ma = i;

    }
    return ma;

}

int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("C-small-1-attempt0.in");
    fout.open("C_Small_N.txt");

    long T;

    fin >> T;


    for(long y=0;y<T;y++)
    {

        long N,K,maxi,left=0,right=0,d;

        fin >> N>>K;

        vector<long> Sub;

        Sub.push_back(N);

        while(K--)
        {

            d = findmax(Sub);
            //cout << Sub[d] <<endl;
            right = Sub[d]/2;
            left = Sub[d]-right;
            left--;
            Sub[d]=-1;
            Sub.push_back(left);
            Sub.push_back(right);

        }

        fout << "Case #"<<y+1<<": "<<max(left,right) << " "<< min(left,right)<<endl;

    }

}
