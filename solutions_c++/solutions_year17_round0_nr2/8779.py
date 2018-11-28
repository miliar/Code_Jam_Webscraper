#include <iostream>
#include<vector>
#include<fstream>

using namespace std;

vector<int> arr;

void int_to_vec(long long int  n)
{
    if(n>0)
    {
        int_to_vec(n/10);
        arr.push_back(int(n%10));
    }
}

int main()
{
    ifstream fin;
    fin.open("in.in");

    ofstream fout;
    fout.open("out.txt");

    long long int n;

    int t;

    fin>>t;

    for(int x=0; x<t; x++)
    {



        arr.clear();

        fin>>n;

        int_to_vec(n);

        int size = arr.size();

        int temp, change = 0;


        for(int i = size - 1; i>0; i--)
        {
            if(arr[i] < arr[i-1])
            {
                change++;
                arr[i-1] -= 1;
                temp = i;
            }
        }

        fout<<"Case #"<<x+1<<": ";

        if(change == 0)
        {
            fout<<n<<endl;
            continue;
        }

        int i=0;

        if(arr[i] == 0)
            i++;

        for( ; i<temp; i++)
            fout<<arr[i];


        for( ; i<size; i++)
            fout<<9;

        fout<<endl;

    }
}


